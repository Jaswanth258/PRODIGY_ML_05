// NutriScan.ai - Application Controller

// DOM elements
const elNavDashboard = document.getElementById('nav-dashboard');
const elNavLogs = document.getElementById('nav-logs');
const elNavModel = document.getElementById('nav-model');

const elDashboardView = document.getElementById('dashboard-view');
const elLogsView = document.getElementById('logs-view');
const elModelView = document.getElementById('model-view');

const elDropZone = document.getElementById('drop-zone');
const elFileInput = document.getElementById('file-input');
const elUploadPrompt = document.getElementById('upload-prompt');
const elPreviewContainer = document.getElementById('preview-container');
const elImagePreview = document.getElementById('image-preview');
const elBtnClearImage = document.getElementById('btn-clear-image');

const elBtnWebcam = document.getElementById('btn-webcam');
const elWebcamContainer = document.getElementById('webcam-container');
const elWebcamVideo = document.getElementById('webcam-video');
const elBtnCapture = document.getElementById('btn-capture');
const elBtnCancelWebcam = document.getElementById('btn-cancel-webcam');

const elBtnAnalyze = document.getElementById('btn-analyze');
const elAnalysisStatus = document.getElementById('analysis-status');
const elStatusText = document.getElementById('status-text');
const elModelSelect = document.getElementById('model-select');

// Results elements
const elResultsEmpty = document.getElementById('results-empty');
const elResultsContent = document.getElementById('results-content');
const elResultFoodName = document.getElementById('result-food-name');
const elBadgeModel = document.getElementById('badge-model');
const elBadgeConfidence = document.getElementById('badge-confidence');
const elResultCalories = document.getElementById('result-calories');
const elPortionWeight = document.getElementById('portion-weight');
const elBtnPortionMinus = document.getElementById('btn-portion-minus');
const elBtnPortionPlus = document.getElementById('btn-portion-plus');
const elRefPortionDesc = document.getElementById('ref-portion-desc');
const elResultDietTip = document.getElementById('result-diet-tip');
const elBtnAddLog = document.getElementById('btn-add-log');

// Macro rings
const elRingProtein = document.getElementById('ring-protein');
const elRingCarbs = document.getElementById('ring-carbs');
const elRingFats = document.getElementById('ring-fats');
const elRingValProtein = document.getElementById('ring-val-protein');
const elRingValCarbs = document.getElementById('ring-val-carbs');
const elRingValFats = document.getElementById('ring-val-fats');

// Summaries
const elSummaryCalories = document.getElementById('summary-calories');
const elSummaryProtein = document.getElementById('summary-protein');
const elSummaryCarbs = document.getElementById('summary-carbs');
const elSummaryFats = document.getElementById('summary-fats');

// Meal logs elements
const elLogTotalCalories = document.getElementById('log-total-calories');
const elLogCaloriesProgress = document.getElementById('log-calories-progress');
const elLogsTableBody = document.getElementById('logs-table-body');
const elBtnClearLogs = document.getElementById('btn-clear-logs');

// Model Center elements
const elCustomModelStatus = document.getElementById('custom-model-status');
const elVitModelStatus = document.getElementById('vit-model-status');
const elVitDownloadInfo = document.getElementById('vit-download-info');
const elBtnRetrain = document.getElementById('btn-retrain');
const elRetrainProgress = document.getElementById('retrain-progress');
const elRetrainStatusText = document.getElementById('retrain-status-text');

// State variables
let activeFile = null;
let activeScanData = null; // Holds the base raw nutrition results
let webcamStream = null;
let currentTab = 'dashboard';
let mealLogs = [];

// Daily nutrition limits
const DAILY_LIMITS = {
    calories: 2000,
    protein: 120,
    carbs: 230,
    fat: 65
};

// Circle circumference for progress rings (radius is 34)
const RING_CIRCUMFERENCE = 2 * Math.PI * 34;

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    // 1. Set current date
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById('current-date').textContent = new Date().toLocaleDateString('en-US', options);

    // 2. Load logs from localStorage
    loadLogs();

    // 3. Tab switching
    initTabs();

    // 4. Drag & Drop events
    initDragAndDrop();

    // 5. Webcam events
    initWebcam();

    // 6. Portion adjuster events
    initPortionAdjuster();

    // 7. Analysis & logging events
    initAnalysis();

    // 8. Model retraining & status polling
    initModelCenter();
    pollModelStatus();
    setInterval(pollModelStatus, 5000);
});

// Tab navigation handler
function initTabs() {
    const tabs = [
        { btn: elNavDashboard, view: elDashboardView, name: 'dashboard' },
        { btn: elNavLogs, view: elLogsView, name: 'logs' },
        { btn: elNavModel, view: elModelView, name: 'model' }
    ];

    tabs.forEach(t => {
        t.btn.addEventListener('click', (e) => {
            e.preventDefault();
            tabs.forEach(o => {
                o.btn.classList.remove('active');
                o.view.style.display = 'none';
            });
            t.btn.classList.add('active');
            t.view.style.display = 'block';
            currentTab = t.name;
            
            if (currentTab === 'logs') {
                renderLogsTable();
            }
            
            // Stop webcam if switching tabs
            if (t.name !== 'dashboard') {
                stopWebcam();
            }
        });
    });
}

// Drag & Drop configuration
function initDragAndDrop() {
    elDropZone.addEventListener('click', (e) => {
        // Prevent click if clicking inner webcam button or cancel buttons
        if (e.target.closest('#btn-webcam') || e.target.closest('.webcam-controls') || e.target.closest('#btn-clear-image')) {
            return;
        }
        elFileInput.click();
    });

    elFileInput.addEventListener('change', () => {
        if (elFileInput.files.length > 0) {
            handleFile(elFileInput.files[0]);
        }
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        elDropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            elDropZone.classList.add('dragover');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        elDropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            elDropZone.classList.remove('dragover');
        }, false);
    });

    elDropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    elBtnClearImage.addEventListener('click', (e) => {
        e.stopPropagation();
        clearFile();
    });
}

function handleFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('Please upload an image file (PNG, JPG, JPEG).');
        return;
    }
    
    stopWebcam();
    activeFile = file;

    const reader = new FileReader();
    reader.onload = (e) => {
        elImagePreview.src = e.target.result;
        elUploadPrompt.style.display = 'none';
        elPreviewContainer.style.display = 'block';
        elBtnAnalyze.disabled = false;
    };
    reader.readAsDataURL(file);
}

function clearFile() {
    activeFile = null;
    elFileInput.value = '';
    elImagePreview.src = '#';
    elPreviewContainer.style.display = 'none';
    elUploadPrompt.style.display = 'flex';
    elBtnAnalyze.disabled = true;
    resetResults();
}

// Webcam support
function initWebcam() {
    elBtnWebcam.addEventListener('click', async (e) => {
        e.stopPropagation();
        clearFile();
        elUploadPrompt.style.display = 'none';
        elWebcamContainer.style.display = 'flex';
        
        try {
            webcamStream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: 'environment', width: 640, height: 480 }
            });
            elWebcamVideo.srcObject = webcamStream;
        } catch (err) {
            console.error('Webcam access error:', err);
            alert('Could not access webcam. Please check your camera permissions.');
            stopWebcam();
            elWebcamContainer.style.display = 'none';
            elUploadPrompt.style.display = 'flex';
        }
    });

    elBtnCancelWebcam.addEventListener('click', (e) => {
        e.stopPropagation();
        stopWebcam();
        elWebcamContainer.style.display = 'none';
        elUploadPrompt.style.display = 'flex';
    });

    elBtnCapture.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!webcamStream) return;

        const canvas = document.createElement('canvas');
        canvas.width = elWebcamVideo.videoWidth || 640;
        canvas.height = elWebcamVideo.videoHeight || 480;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(elWebcamVideo, 0, 0, canvas.width, canvas.height);

        canvas.toBlob((blob) => {
            const file = new File([blob], "webcam_capture.jpg", { type: "image/jpeg" });
            handleFile(file);
        }, 'image/jpeg');
    });
}

function stopWebcam() {
    if (webcamStream) {
        webcamStream.getTracks().forEach(track => track.stop());
        webcamStream = null;
        elWebcamVideo.srcObject = null;
    }
}

// Analysis API Integration
function initAnalysis() {
    elBtnAnalyze.addEventListener('click', async () => {
        if (!activeFile) return;

        resetResults();
        elBtnAnalyze.disabled = true;
        elAnalysisStatus.style.display = 'flex';
        elStatusText.textContent = "Scanning image and running inference...";

        const formData = new FormData();
        formData.append('image', activeFile);
        formData.append('model', elModelSelect.value);

        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.status === 202) {
                // ViT loading scenario
                elStatusText.textContent = data.message;
                // Retry loop logic
                let retries = 5;
                const interval = setInterval(async () => {
                    if (retries <= 0) {
                        clearInterval(interval);
                        elAnalysisStatus.style.display = 'none';
                        elBtnAnalyze.disabled = false;
                        alert("Inference took too long to compile. Please try again.");
                        return;
                    }
                    retries--;
                    elStatusText.textContent = "Model downloading weights. Compiling layers (" + retries + ")...";
                    
                    try {
                        const checkResponse = await fetch('/api/predict', { method: 'POST', body: formData });
                        const checkData = await checkResponse.json();
                        if (checkResponse.status === 200) {
                            clearInterval(interval);
                            displayResults(checkData);
                        }
                    } catch(e) {}
                }, 5000);
            } else if (response.ok) {
                displayResults(data);
            } else {
                alert(data.error || 'Server error during food analysis');
                elAnalysisStatus.style.display = 'none';
                elBtnAnalyze.disabled = false;
            }
        } catch (error) {
            console.error('Analysis error:', error);
            alert('Failed to connect to the server. Make sure Flask app.py is running.');
            elAnalysisStatus.style.display = 'none';
            elBtnAnalyze.disabled = false;
        }
    });

    elBtnAddLog.addEventListener('click', () => {
        if (!activeScanData) return;

        const portionG = parseInt(elPortionWeight.value) || 100;
        const scale = portionG / 100;

        const logItem = {
            id: Date.now(),
            name: activeScanData.predicted_class,
            model: activeScanData.model_used === 'vit' ? 'Vision Transformer' : 'Custom ML',
            portion: portionG,
            protein: parseFloat((activeScanData.nutrition.protein * scale).toFixed(1)),
            carbs: parseFloat((activeScanData.nutrition.carbs * scale).toFixed(1)),
            fats: parseFloat((activeScanData.nutrition.fat * scale).toFixed(1)),
            calories: Math.round(activeScanData.nutrition.calories_per_100g * scale),
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        };

        mealLogs.push(logItem);
        saveLogs();
        updateSummaryStats();
        
        // Show brief success alert
        const originalText = elBtnAddLog.innerHTML;
        elBtnAddLog.innerHTML = '<i class="fa-solid fa-circle-check"></i> Added Successfully!';
        elBtnAddLog.style.background = 'var(--protein-color)';
        setTimeout(() => {
            elBtnAddLog.innerHTML = originalText;
            elBtnAddLog.style.background = '';
        }, 1500);
    });

    elBtnClearLogs.addEventListener('click', () => {
        if (confirm("Are you sure you want to clear today's food logs?")) {
            mealLogs = [];
            saveLogs();
            updateSummaryStats();
            renderLogsTable();
        }
    });
}

function displayResults(data) {
    activeScanData = data;
    elAnalysisStatus.style.display = 'none';
    elBtnAnalyze.disabled = false;

    // Show panel
    elResultsEmpty.style.display = 'none';
    elResultsContent.style.display = 'flex';

    // Populate header info
    elResultFoodName.textContent = data.predicted_class;
    elBadgeModel.textContent = data.model_used === 'vit' ? 'Vision Transformer (101)' : 'Custom ML (4)';
    elBadgeConfidence.textContent = 'Confidence: ' + (data.confidence * 100).toFixed(1) + '%';
    
    // Set portion and database description
    elPortionWeight.value = data.nutrition.serving_size;
    elRefPortionDesc.textContent = data.nutrition.description;
    elResultDietTip.textContent = data.nutrition.suggestion;

    updatePortionMath();
}

function resetResults() {
    activeScanData = null;
    elResultsContent.style.display = 'none';
    elResultsEmpty.style.display = 'flex';
}

// Portion Adjuster calculations
function initPortionAdjuster() {
    elBtnPortionMinus.addEventListener('click', () => {
        let val = parseInt(elPortionWeight.value) || 100;
        val = Math.max(10, val - 25);
        elPortionWeight.value = val;
        updatePortionMath();
    });

    elBtnPortionPlus.addEventListener('click', () => {
        let val = parseInt(elPortionWeight.value) || 100;
        val = Math.min(1000, val + 25);
        elPortionWeight.value = val;
        updatePortionMath();
    });

    elPortionWeight.addEventListener('input', () => {
        let val = parseInt(elPortionWeight.value);
        if (isNaN(val) || val <= 0) val = 100;
        updatePortionMath();
    });
}

function updatePortionMath() {
    if (!activeScanData) return;

    const portionG = parseInt(elPortionWeight.value) || 100;
    const scale = portionG / 100;

    // 1. Update Calories
    const cals = Math.round(activeScanData.nutrition.calories_per_100g * scale);
    elResultCalories.textContent = cals;

    // 2. Update Macros
    const p = activeScanData.nutrition.protein * scale;
    const c = activeScanData.nutrition.carbs * scale;
    const f = activeScanData.nutrition.fat * scale;

    elRingValProtein.textContent = p.toFixed(1) + 'g';
    elRingValCarbs.textContent = c.toFixed(1) + 'g';
    elRingValFats.textContent = f.toFixed(1) + 'g';

    // 3. Update Progress rings offsets
    setProgressRing(elRingProtein, p, DAILY_LIMITS.protein);
    setProgressRing(elRingCarbs, c, DAILY_LIMITS.carbs);
    setProgressRing(elRingFats, f, DAILY_LIMITS.fat);
}

function setProgressRing(ringElement, value, limit) {
    const percent = Math.min(100, (value / limit) * 100);
    const offset = RING_CIRCUMFERENCE - (percent / 100) * RING_CIRCUMFERENCE;
    ringElement.style.strokeDasharray = `${RING_CIRCUMFERENCE} ${RING_CIRCUMFERENCE}`;
    ringElement.style.strokeDashoffset = offset;
}

// LocalStorage Sync
function saveLogs() {
    localStorage.setItem('nutriscan_logs', JSON.stringify(mealLogs));
}

function loadLogs() {
    const saved = localStorage.getItem('nutriscan_logs');
    if (saved) {
        try {
            mealLogs = JSON.parse(saved);
        } catch (e) {
            mealLogs = [];
        }
    }
    updateSummaryStats();
}

function updateSummaryStats() {
    let totCalories = 0;
    let totProtein = 0;
    let totCarbs = 0;
    let totFats = 0;

    mealLogs.forEach(item => {
        totCalories += item.calories;
        totProtein += item.protein;
        totCarbs += item.carbs;
        totFats += item.fats;
    });

    // Update Dashboard values
    elSummaryCalories.textContent = totCalories;
    elSummaryProtein.textContent = totProtein.toFixed(1);
    elSummaryCarbs.textContent = totCarbs.toFixed(1);
    elSummaryFats.textContent = totFats.toFixed(1);

    // Update Journal values
    elLogTotalCalories.textContent = totCalories;
    const calPercent = Math.min(100, (totCalories / DAILY_LIMITS.calories) * 100);
    elLogCaloriesProgress.style.width = calPercent + '%';
    
    // Set color based on limit
    if (totCalories > DAILY_LIMITS.calories) {
        elLogCaloriesProgress.style.background = '#ef4444'; // Red if exceeded
    } else {
        elLogCaloriesProgress.style.background = 'var(--accent-gradient)';
    }
}

function renderLogsTable() {
    elLogsTableBody.innerHTML = '';

    if (mealLogs.length === 0) {
        elLogsTableBody.innerHTML = `
            <tr class="no-logs">
                <td colspan="9" style="text-align: center; padding: 40px 0; color: #8a99ad;">
                    <i class="fa-solid fa-utensils" style="font-size: 32px; margin-bottom: 12px; display: block; opacity: 0.5;"></i>
                    No meals logged for today. Scan food items to add them here!
                </td>
            </tr>
        `;
        return;
    }

    mealLogs.forEach((item, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><strong>${item.name}</strong></td>
            <td><span class="badge" style="background-color: ${item.model === 'Vision Transformer' ? 'rgba(139, 92, 246, 0.1)' : 'rgba(59, 130, 246, 0.1)'}; color: ${item.model === 'Vision Transformer' ? '#a78bfa' : '#60a5fa'}; border: none;">${item.model}</span></td>
            <td>${item.portion}g</td>
            <td>${item.protein.toFixed(1)}g</td>
            <td>${item.carbs.toFixed(1)}g</td>
            <td>${item.fats.toFixed(1)}g</td>
            <td><strong>${item.calories} kcal</strong></td>
            <td style="color: var(--text-muted);">${item.timestamp}</td>
            <td>
                <button class="delete-btn" onclick="deleteLogItem(${item.id})" title="Delete entry">
                    <i class="fa-solid fa-circle-minus"></i>
                </button>
            </td>
        `;
        elLogsTableBody.appendChild(tr);
    });
}

window.deleteLogItem = function(id) {
    mealLogs = mealLogs.filter(item => item.id !== id);
    saveLogs();
    updateSummaryStats();
    renderLogsTable();
};

// Model Center Tab Actions
function initModelCenter() {
    elBtnRetrain.addEventListener('click', async () => {
        if (elBtnRetrain.disabled) return;

        elBtnRetrain.disabled = true;
        elRetrainProgress.style.display = 'flex';
        elRetrainStatusText.textContent = "Pipeline initialized. Downloading images / creating synthetic fallbacks...";

        try {
            const response = await fetch('/api/train_custom', {
                method: 'POST'
            });

            if (response.ok) {
                elRetrainStatusText.textContent = "Training models (Random Forest, SVM, GBDT)...";
                pollModelStatus();
            } else {
                alert("Could not start retraining.");
                elBtnRetrain.disabled = false;
                elRetrainProgress.style.display = 'none';
            }
        } catch (e) {
            console.error("Retrain connection error:", e);
            elBtnRetrain.disabled = false;
            elRetrainProgress.style.display = 'none';
        }
    });
}

async function pollModelStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();

        // 1. Custom model label
        if (data.custom_model_loaded) {
            elCustomModelStatus.textContent = "Active (" + data.custom_model_name + ")";
            elCustomModelStatus.className = "status-badge success";
        } else {
            elCustomModelStatus.textContent = "Not Trained";
            elCustomModelStatus.className = "status-badge failed";
        }

        // 2. ViT model label
        if (data.vit_model_loaded) {
            elVitModelStatus.textContent = "Ready / Cached";
            elVitModelStatus.className = "status-badge success";
            elVitDownloadInfo.style.display = 'none';
        } else if (data.vit_model_loading) {
            elVitModelStatus.textContent = "Loading Weights...";
            elVitModelStatus.className = "status-badge info";
            elVitDownloadInfo.style.display = 'block';
        } else {
            elVitModelStatus.textContent = "Idle (Click Analyze to Load)";
            elVitModelStatus.className = "status-badge info";
            elVitDownloadInfo.style.display = 'block';
        }

        // 3. Retrain status
        if (data.custom_training_status === "running") {
            elBtnRetrain.disabled = true;
            elRetrainProgress.style.display = 'flex';
            elRetrainStatusText.textContent = "Training models in background. Compiling shape HOG matrices...";
        } else if (data.custom_training_status === "success") {
            elBtnRetrain.disabled = false;
            elRetrainProgress.style.display = 'none';
            elCustomModelStatus.textContent = "Active (Retrained)";
            elCustomModelStatus.className = "status-badge success";
        } else if (data.custom_training_status.startsWith("failed")) {
            elBtnRetrain.disabled = false;
            elRetrainProgress.style.display = 'none';
            alert("Model retraining failed: " + data.custom_training_status);
        }
    } catch (e) {
        console.error("Status polling failed:", e);
    }
}
