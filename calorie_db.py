# Food Calorie and Macronutrient Database for Food-101 classes and Prototype classes

NUTRITION_DB = {
    # Custom/Prototype classes
    "apple": {
        "calories_per_100g": 52,
        "serving_size": 150,
        "description": "1 Medium Apple (150g)",
        "protein": 0.3,
        "fat": 0.2,
        "carbs": 14.0,
        "suggestion": "Rich in fiber and vitamin C. Excellent healthy snack to regulate blood sugar levels."
    },
    "burger": {
        "calories_per_100g": 295,
        "serving_size": 200,
        "description": "1 Cheeseburger (200g)",
        "protein": 17.0,
        "fat": 14.0,
        "carbs": 24.0,
        "suggestion": "Moderate in protein but high in saturated fats. Balance with a light, vegetable-based side."
    },
    "pizza": {
        "calories_per_100g": 266,
        "serving_size": 250,
        "description": "1 Personal Pizza (250g)",
        "protein": 11.0,
        "fat": 10.0,
        "carbs": 33.0,
        "suggestion": "Calorie-dense with high carbs and sodium. Try adding vegetable toppings to boost fiber."
    },
    "salad": {
        "calories_per_100g": 45,
        "serving_size": 150,
        "description": "1 Bowl of Green Salad (150g)",
        "protein": 1.5,
        "fat": 2.0,
        "carbs": 5.0,
        "suggestion": "Low in calories, high in vitamins and fiber. Be mindful of high-calorie creamy dressings."
    },

    # Food-101 classes
    "apple_pie": {
        "calories_per_100g": 237,
        "serving_size": 125,
        "description": "1 slice of Apple Pie (125g)",
        "protein": 2.4,
        "fat": 11.0,
        "carbs": 34.0,
        "suggestion": "High in sugars and fats. Enjoy in moderation as a dessert."
    },
    "baby_back_ribs": {
        "calories_per_100g": 312,
        "serving_size": 200,
        "description": "1 serving of Ribs (200g)",
        "protein": 21.0,
        "fat": 24.0,
        "carbs": 3.0,
        "suggestion": "Rich in protein and iron, but very high in fats. Watch the sugary BBQ sauces."
    },
    "baklava": {
        "calories_per_100g": 428,
        "serving_size": 80,
        "description": "2 pieces of Baklava (80g)",
        "protein": 6.0,
        "fat": 23.0,
        "carbs": 51.0,
        "suggestion": "Extremely calorie-dense dessert loaded with nuts, honey, and phyllo pastry. Limit portion sizes."
    },
    "beef_carpaccio": {
        "calories_per_100g": 135,
        "serving_size": 100,
        "description": "1 plate of Beef Carpaccio (100g)",
        "protein": 20.0,
        "fat": 5.5,
        "carbs": 1.0,
        "suggestion": "Excellent source of high-quality lean protein and iron. Best served with rocket and olive oil."
    },
    "beef_tartare": {
        "calories_per_100g": 160,
        "serving_size": 120,
        "description": "1 portion of Beef Tartare (120g)",
        "protein": 19.5,
        "fat": 9.0,
        "carbs": 1.5,
        "suggestion": "High-protein dish. Ensure meat is of high quality and fresh to prevent bacterial risks."
    },
    "beet_salad": {
        "calories_per_100g": 85,
        "serving_size": 150,
        "description": "1 serving of Beet Salad (150g)",
        "protein": 2.0,
        "fat": 4.5,
        "carbs": 9.0,
        "suggestion": "High in folate, antioxidants, and nitrates. Helps improve blood pressure and circulation."
    },
    "beignets": {
        "calories_per_100g": 360,
        "serving_size": 90,
        "description": "3 Beignets (90g)",
        "protein": 5.0,
        "fat": 18.0,
        "carbs": 45.0,
        "suggestion": "Fried pastry coated in powdered sugar. High in simple carbs and trans fats. Eat occasionally."
    },
    "bibimbap": {
        "calories_per_100g": 135,
        "serving_size": 400,
        "description": "1 Bowl of Bibimbap (400g)",
        "protein": 6.5,
        "fat": 3.5,
        "carbs": 20.0,
        "suggestion": "Highly nutritious Korean dish. Contains a good balance of protein, carbs, and assorted vegetables."
    },
    "bread_pudding": {
        "calories_per_100g": 270,
        "serving_size": 150,
        "description": "1 slice of Bread Pudding (150g)",
        "protein": 5.0,
        "fat": 11.0,
        "carbs": 38.0,
        "suggestion": "Sweet comfort food dessert. Moderately high in carbohydrates, fats, and refined sugar."
    },
    "bruschetta": {
        "calories_per_100g": 168,
        "serving_size": 100,
        "description": "3 pieces of Bruschetta (100g)",
        "protein": 4.0,
        "fat": 6.0,
        "carbs": 24.0,
        "suggestion": "Good light appetizer containing tomatoes, garlic, and olive oil. High in lycopene."
    },
    "caesar_salad": {
        "calories_per_100g": 180,
        "serving_size": 200,
        "description": "1 large Caesar Salad (200g)",
        "protein": 5.0,
        "fat": 15.0,
        "carbs": 7.0,
        "suggestion": "High in fats due to the creamy Caesar dressing and croutons. Add grilled chicken for extra protein."
    },
    "caprese_salad": {
        "calories_per_100g": 130,
        "serving_size": 150,
        "description": "1 serving of Caprese (150g)",
        "protein": 6.5,
        "fat": 10.0,
        "carbs": 3.5,
        "suggestion": "High in healthy fats from olive oil and calcium from mozzarella. Low in carbs."
    },
    "carrot_cake": {
        "calories_per_100g": 415,
        "serving_size": 120,
        "description": "1 slice of Carrot Cake (120g)",
        "protein": 4.5,
        "fat": 22.0,
        "carbs": 50.0,
        "suggestion": "Contains carrots, but the high oil, sugar, and cream cheese frosting make it very calorie-dense."
    },
    "ceviche": {
        "calories_per_100g": 90,
        "serving_size": 180,
        "description": "1 portion of Ceviche (180g)",
        "protein": 16.0,
        "fat": 1.5,
        "carbs": 4.0,
        "suggestion": "An excellent clean, lean protein source. Low in calories, refreshing and rich in citrus antioxidants."
    },
    "cheesecake": {
        "calories_per_100g": 321,
        "serving_size": 125,
        "description": "1 slice of Cheesecake (125g)",
        "protein": 5.5,
        "fat": 22.5,
        "carbs": 25.5,
        "suggestion": "High in saturated fats and refined sugars. Enjoy in small portions occasionally."
    },
    "cheese_plate": {
        "calories_per_100g": 380,
        "serving_size": 100,
        "description": "1 Cheese Board platter (100g)",
        "protein": 22.0,
        "fat": 32.0,
        "carbs": 2.0,
        "suggestion": "Excellent source of calcium and proteins, but very calorie-dense. Watch serving size."
    },
    "chicken_curry": {
        "calories_per_100g": 130,
        "serving_size": 300,
        "description": "1 bowl of Chicken Curry (300g)",
        "protein": 14.0,
        "fat": 6.5,
        "carbs": 4.0,
        "suggestion": "Rich in protein and thermogenic spices like turmeric. Enjoy with brown rice or quinoa."
    },
    "chicken_quesadilla": {
        "calories_per_100g": 290,
        "serving_size": 220,
        "description": "1 Chicken Quesadilla (220g)",
        "protein": 17.5,
        "fat": 14.5,
        "carbs": 23.0,
        "suggestion": "High protein and energy, but cheese content increases sodium and fats. Limit extra sour cream."
    },
    "chicken_wings": {
        "calories_per_100g": 290,
        "serving_size": 180,
        "description": "6 Chicken Wings (180g)",
        "protein": 22.0,
        "fat": 20.0,
        "carbs": 4.0,
        "suggestion": "Good protein source, but deep-frying and heavy sauces add substantial fat and calories. Bake them for health."
    },
    "chocolate_cake": {
        "calories_per_100g": 389,
        "serving_size": 100,
        "description": "1 slice of Chocolate Cake (100g)",
        "protein": 4.0,
        "fat": 18.0,
        "carbs": 53.0,
        "suggestion": "Highly refined carbs and sugars. Enjoy as a celebratory indulgence."
    },
    "chocolate_mousse": {
        "calories_per_100g": 225,
        "serving_size": 90,
        "description": "1 cup of Chocolate Mousse (90g)",
        "protein": 3.0,
        "fat": 15.0,
        "carbs": 20.0,
        "suggestion": "Rich in flavor, light in texture, but high in dairy fats and sugars. Watch the portions."
    },
    "churros": {
        "calories_per_100g": 383,
        "serving_size": 80,
        "description": "3 pieces of Churros (80g)",
        "protein": 4.0,
        "fat": 20.0,
        "carbs": 47.0,
        "suggestion": "Deep-fried dough rolled in sugar. High in empty calories and fat. Best shared."
    },
    "clam_chowder": {
        "calories_per_100g": 120,
        "serving_size": 240,
        "description": "1 cup of Clam Chowder (240g)",
        "protein": 6.0,
        "fat": 8.0,
        "carbs": 10.0,
        "suggestion": "Cream-based soup containing seafood. High in sodium and fat; choose tomato-based Manhattan chowder if dieting."
    },
    "club_sandwich": {
        "calories_per_100g": 220,
        "serving_size": 250,
        "description": "1 Club Sandwich (250g)",
        "protein": 14.0,
        "fat": 11.0,
        "carbs": 18.0,
        "suggestion": "A good balance of nutrients. Avoid extra mayonnaise and opt for whole wheat bread if possible."
    },
    "crab_cakes": {
        "calories_per_100g": 210,
        "serving_size": 150,
        "description": "2 Crab Cakes (150g)",
        "protein": 15.0,
        "fat": 11.0,
        "carbs": 13.0,
        "suggestion": "Rich in lean seafood protein and selenium. Lightly pan-searing is healthier than deep-frying."
    },
    "creme_brulee": {
        "calories_per_100g": 300,
        "serving_size": 120,
        "description": "1 ramekin of Creme Brulee (120g)",
        "protein": 4.0,
        "fat": 25.0,
        "carbs": 15.0,
        "suggestion": "Rich custard dessert made of egg yolks and heavy cream. Very high in fats and cholesterol."
    },
    "croque_madame": {
        "calories_per_100g": 260,
        "serving_size": 250,
        "description": "1 Croque Madame (250g)",
        "protein": 16.0,
        "fat": 15.0,
        "carbs": 18.0,
        "suggestion": "Toasted ham and cheese sandwich topped with fried egg and bechamel sauce. Heavy in fats."
    },
    "cup_cakes": {
        "calories_per_100g": 380,
        "serving_size": 70,
        "description": "1 standard Cupcake (70g)",
        "protein": 3.0,
        "fat": 16.0,
        "carbs": 55.0,
        "suggestion": "Very high in sugar and butter frosting. Portion control is key."
    },
    "beef_carpaccio": {
        "calories_per_100g": 135,
        "serving_size": 100,
        "description": "1 plate of Beef Carpaccio (100g)",
        "protein": 20.0,
        "fat": 5.5,
        "carbs": 1.0,
        "suggestion": "Excellent high-protein, low-carb choice. Served with olive oil and capers."
    },
    "deviled_eggs": {
        "calories_per_100g": 200,
        "serving_size": 90,
        "description": "3 Deviled Egg halves (90g)",
        "protein": 11.0,
        "fat": 16.0,
        "carbs": 1.0,
        "suggestion": "Rich in healthy egg fats, choline, and protein. Keep mayonnaise content moderate."
    },
    "donuts": {
        "calories_per_100g": 417,
        "serving_size": 60,
        "description": "1 medium Donut (60g)",
        "protein": 4.5,
        "fat": 22.0,
        "carbs": 51.0,
        "suggestion": "Fried dough high in sugar and refined fats. High glycemic load. Eat sparingly."
    },
    "dumplings": {
        "calories_per_100g": 175,
        "serving_size": 150,
        "description": "5 steamed Dumplings (150g)",
        "protein": 8.0,
        "fat": 6.0,
        "carbs": 22.0,
        "suggestion": "Steamed dumplings are much healthier and lower in calorie than fried versions."
    },
    "edamame": {
        "calories_per_100g": 122,
        "serving_size": 100,
        "description": "1 cup of Edamame pods (100g)",
        "protein": 11.0,
        "fat": 5.0,
        "carbs": 10.0,
        "suggestion": "Fantastic plant-based protein, fiber, and iron. Highly recommended healthy snack."
    },
    "eggs_benedict": {
        "calories_per_100g": 210,
        "serving_size": 250,
        "description": "1 serving of Eggs Benedict (250g)",
        "protein": 11.5,
        "fat": 15.0,
        "carbs": 11.0,
        "suggestion": "Contains good egg protein, but hollandaise sauce adds a high amount of butter fat. Watch sodium."
    },
    "escargots": {
        "calories_per_100g": 140,
        "serving_size": 100,
        "description": "6 Escargots in butter (100g)",
        "protein": 14.0,
        "fat": 9.0,
        "carbs": 2.0,
        "suggestion": "High protein, low carb snail meat, but traditionally prepared in rich garlic butter."
    },
    "falafel": {
        "calories_per_100g": 330,
        "serving_size": 150,
        "description": "4 pieces of Falafel (150g)",
        "protein": 13.0,
        "fat": 17.0,
        "carbs": 32.0,
        "suggestion": "Good plant-based protein and fiber from chickpeas, though deep-frying adds calories."
    },
    "filet_mignon": {
        "calories_per_100g": 220,
        "serving_size": 200,
        "description": "1 Filet Mignon steak (200g)",
        "protein": 26.0,
        "fat": 12.0,
        "carbs": 0.0,
        "suggestion": "Very tender, high-quality lean protein, rich in zinc and B12. Perfect keto-friendly entree."
    },
    "fish_and_chips": {
        "calories_per_100g": 240,
        "serving_size": 350,
        "description": "1 serving of Fish & Chips (350g)",
        "protein": 12.0,
        "fat": 13.0,
        "carbs": 20.0,
        "suggestion": "Calorie-dense pub classic. The deep-fried batter and potato chips carry high trans fats."
    },
    "foie_gras": {
        "calories_per_100g": 462,
        "serving_size": 50,
        "description": "1 slice of Foie Gras (50g)",
        "protein": 11.0,
        "fat": 44.0,
        "carbs": 4.5,
        "suggestion": "Extremely calorie-dense duck liver. Very high in monounsaturated and saturated fats."
    },
    "beef_tartare": {
        "calories_per_100g": 160,
        "serving_size": 120,
        "description": "1 serving of Beef Tartare (120g)",
        "protein": 19.5,
        "fat": 9.0,
        "carbs": 1.5,
        "suggestion": "High protein food, make sure it is fresh beef from reliable sources."
    },
    "french_fries": {
        "calories_per_100g": 312,
        "serving_size": 150,
        "description": "1 large serving of Fries (150g)",
        "protein": 3.4,
        "fat": 15.0,
        "carbs": 41.0,
        "suggestion": "Deep fried starch. High glycemic index and fat content. Limit portion size."
    },
    "french_onion_soup": {
        "calories_per_100g": 75,
        "serving_size": 250,
        "description": "1 bowl of French Onion Soup (250g)",
        "protein": 4.0,
        "fat": 4.5,
        "carbs": 6.0,
        "suggestion": "Relatively low in calories, but croutons and cheese crust raise carbs and fats. High in sodium."
    },
    "french_toast": {
        "calories_per_100g": 229,
        "serving_size": 180,
        "description": "2 slices of French Toast (180g)",
        "protein": 6.5,
        "fat": 8.0,
        "carbs": 33.0,
        "suggestion": "Made with eggs, milk, and bread. Calorie count increases rapidly with maple syrup and butter."
    },
    "fried_calamari": {
        "calories_per_100g": 175,
        "serving_size": 150,
        "description": "1 serving of Fried Calamari (150g)",
        "protein": 15.0,
        "fat": 9.0,
        "carbs": 8.0,
        "suggestion": "Good protein, but deep-frying squid in flour batter adds substantial carbs and fats."
    },
    "fried_rice": {
        "calories_per_100g": 163,
        "serving_size": 250,
        "description": "1 bowl of Fried Rice (250g)",
        "protein": 4.0,
        "fat": 4.0,
        "carbs": 28.0,
        "suggestion": "High in fast-digesting carbohydrates and sodium. Add extra vegetables and egg to improve macros."
    },
    "frozen_yogurt": {
        "calories_per_100g": 159,
        "serving_size": 120,
        "description": "1 serving of Frozen Yogurt (120g)",
        "protein": 4.0,
        "fat": 3.0,
        "carbs": 29.0,
        "suggestion": "Often considered healthier than ice cream, but contains high amount of sugars. Choose low-sugar toppings."
    },
    "garlic_bread": {
        "calories_per_100g": 350,
        "serving_size": 80,
        "description": "2 slices of Garlic Bread (80g)",
        "protein": 7.0,
        "fat": 16.0,
        "carbs": 43.0,
        "suggestion": "High in carbohydrates and fats from butter. Eat in moderation alongside high-protein meals."
    },
    "gnocchi": {
        "calories_per_100g": 132,
        "serving_size": 200,
        "description": "1 bowl of Gnocchi (200g)",
        "protein": 3.0,
        "fat": 3.0,
        "carbs": 24.0,
        "suggestion": "Dense potato-based pasta. Carbs and calories climb quickly depending on cheese or butter sauces."
    },
    "greek_salad": {
        "calories_per_100g": 115,
        "serving_size": 180,
        "description": "1 bowl of Greek Salad (180g)",
        "protein": 3.0,
        "fat": 9.0,
        "carbs": 5.0,
        "suggestion": "Highly nutritious with tomatoes, olives, cucumbers, and feta. Rich in monounsaturated olive oil fats."
    },
    "grilled_cheese_sandwich": {
        "calories_per_100g": 320,
        "serving_size": 130,
        "description": "1 Grilled Cheese (130g)",
        "protein": 11.0,
        "fat": 17.0,
        "carbs": 31.0,
        "suggestion": "High in carbohydrates and saturated fats. Best prepared with whole grain bread and low-fat cheese."
    },
    "beet_salad": {
        "calories_per_100g": 85,
        "serving_size": 150,
        "description": "1 serving of Beet Salad (150g)",
        "protein": 2.0,
        "fat": 4.5,
        "carbs": 9.0,
        "suggestion": "Beets contain iron and fiber. Good healthy vegetarian side dish."
    },
    "grilled_salmon": {
        "calories_per_100g": 206,
        "serving_size": 170,
        "description": "1 Salmon Fillet (170g)",
        "protein": 22.0,
        "fat": 12.0,
        "carbs": 0.0,
        "suggestion": "Excellent protein source. Superb levels of anti-inflammatory Omega-3 fatty acids. Highly recommended."
    },
    "guacamole": {
        "calories_per_100g": 157,
        "serving_size": 80,
        "description": "1 dip serving of Guacamole (80g)",
        "protein": 2.0,
        "fat": 14.0,
        "carbs": 8.0,
        "suggestion": "Rich in cardiovascular-friendly monounsaturated fats, potassium, and fiber. Watch high-salt dipping chips."
    },
    "gyoza": {
        "calories_per_100g": 200,
        "serving_size": 150,
        "description": "6 pieces of Gyoza (150g)",
        "protein": 8.0,
        "fat": 8.0,
        "carbs": 24.0,
        "suggestion": "Steamed and lightly pan-seared. Gives a moderate balance of protein and carbs. Watch dipping sauce sodium."
    },
    "hamburger": {
        "calories_per_100g": 264,
        "serving_size": 180,
        "description": "1 standard Hamburger (180g)",
        "protein": 14.5,
        "fat": 10.0,
        "carbs": 28.0,
        "suggestion": "Provides high protein and iron. Can be a solid meal if cooked with lean meat and light toppings."
    },
    "hot_and_sour_soup": {
        "calories_per_100g": 50,
        "serving_size": 250,
        "description": "1 bowl of Hot & Sour Soup (250g)",
        "protein": 3.0,
        "fat": 2.0,
        "carbs": 6.0,
        "suggestion": "Low calorie starter. Loaded with wood ear mushrooms, tofu, and spices. Watch sodium content."
    },
    "hot_dog": {
        "calories_per_100g": 290,
        "serving_size": 120,
        "description": "1 Hot Dog with Bun (120g)",
        "protein": 10.0,
        "fat": 16.0,
        "carbs": 26.0,
        "suggestion": "Processed meats carry high sodium and nitrates. Eat sparingly and choose mustard over sugary sauces."
    },
    "huevos_rancheros": {
        "calories_per_100g": 150,
        "serving_size": 300,
        "description": "1 plate of Huevos Rancheros (300g)",
        "protein": 9.0,
        "fat": 8.5,
        "carbs": 11.0,
        "suggestion": "A highly energetic breakfast containing protein-rich eggs, beans, corn tortillas, and salsa."
    },
    "hummus": {
        "calories_per_100g": 166,
        "serving_size": 50,
        "description": "2 tbsp of Hummus (50g)",
        "protein": 8.0,
        "fat": 10.0,
        "carbs": 14.0,
        "suggestion": "Healthy Middle Eastern spread rich in plant protein, dietary fiber, and healthy sesame fats."
    },
    "ice_cream": {
        "calories_per_100g": 207,
        "serving_size": 100,
        "description": "1 scoop of Ice Cream (100g)",
        "protein": 3.5,
        "fat": 11.0,
        "carbs": 24.0,
        "suggestion": "High in milk fat and simple sugars. Portion control is essential to avoid calorie spikes."
    },
    "lasagna": {
        "calories_per_100g": 135,
        "serving_size": 350,
        "description": "1 slice of Meat Lasagna (350g)",
        "protein": 12.0,
        "fat": 6.0,
        "carbs": 9.5,
        "suggestion": "Substantial meal offering protein and carbs, but can be high in saturated fats and sodium due to cheese."
    },
    "beignets": {
        "calories_per_100g": 360,
        "serving_size": 90,
        "description": "3 Beignets (90g)",
        "protein": 5.0,
        "fat": 18.0,
        "carbs": 45.0,
        "suggestion": "Fried sweet pastry. High in saturated fats and sugars. Enjoy sparingly."
    },
    "lobster_bisque": {
        "calories_per_100g": 130,
        "serving_size": 240,
        "description": "1 cup of Lobster Bisque (240g)",
        "protein": 7.0,
        "fat": 9.0,
        "carbs": 6.0,
        "suggestion": "Rich, creamy lobster soup. High in cholesterol and saturated fats from heavy cream base."
    },
    "lobster_roll_sandwich": {
        "calories_per_100g": 230,
        "serving_size": 200,
        "description": "1 Lobster Roll (200g)",
        "protein": 16.0,
        "fat": 12.0,
        "carbs": 15.0,
        "suggestion": "Provides high protein lobster meat, but mayonnaise dressing and buttered brioche bun add fat."
    },
    "macaroni_and_cheese": {
        "calories_per_100g": 370,
        "serving_size": 250,
        "description": "1 bowl of Mac & Cheese (250g)",
        "protein": 14.0,
        "fat": 16.0,
        "carbs": 43.0,
        "suggestion": "High in refined carbohydrates, sodium, and fats. Eat occasionally or seek whole wheat options."
    },
    "macarons": {
        "calories_per_100g": 450,
        "serving_size": 30,
        "description": "3 French Macarons (30g)",
        "protein": 7.0,
        "fat": 20.0,
        "carbs": 60.0,
        "suggestion": "Gluten-free almond meal pastry, but highly sweet and sugar-packed. Portions should be small."
    },
    "miso_soup": {
        "calories_per_100g": 35,
        "serving_size": 200,
        "description": "1 bowl of Miso Soup (200g)",
        "protein": 2.5,
        "fat": 1.0,
        "carbs": 3.5,
        "suggestion": "Very low calorie fermented broth containing gut-friendly probiotics. Watch high sodium levels."
    },
    "mussels": {
        "calories_per_100g": 172,
        "serving_size": 150,
        "description": "1 plate of Steamed Mussels (150g)",
        "protein": 24.0,
        "fat": 4.5,
        "carbs": 7.0,
        "suggestion": "Excellent source of lean protein, zinc, selenium, and vitamin B12. Steamed version is very healthy."
    },
    "nachos": {
        "calories_per_100g": 343,
        "serving_size": 200,
        "description": "1 plate of Cheese Nachos (200g)",
        "protein": 8.0,
        "fat": 19.0,
        "carbs": 36.0,
        "suggestion": "Highly processed snack. Cheese and corn tortilla chips contain high amounts of fats and sodium."
    },
    "omelette": {
        "calories_per_100g": 154,
        "serving_size": 150,
        "description": "3-Egg Omelette (150g)",
        "protein": 11.0,
        "fat": 12.0,
        "carbs": 1.0,
        "suggestion": "Excellent source of protein, healthy fats, and vitamins. Add spinach, onion, and tomato for fiber."
    },
    "onion_rings": {
        "calories_per_100g": 411,
        "serving_size": 120,
        "description": "1 basket of Onion Rings (120g)",
        "protein": 4.0,
        "fat": 20.0,
        "carbs": 44.0,
        "suggestion": "Deep-fried snack. Contains high amount of oil, fats, and flour carbohydrates."
    },
    "oysters": {
        "calories_per_100g": 81,
        "serving_size": 100,
        "description": "6 Raw Oysters (100g)",
        "protein": 9.5,
        "fat": 2.3,
        "carbs": 5.0,
        "suggestion": "Extremely high in zinc, lean proteins, and minerals. Steer clear of heavy cream toppings."
    },
    "bibimbap": {
        "calories_per_100g": 135,
        "serving_size": 400,
        "description": "1 Bowl of Bibimbap (400g)",
        "protein": 6.5,
        "fat": 3.5,
        "carbs": 20.0,
        "suggestion": "Nutritious combination of rice, vegetables, egg, and meat. Excellent meal."
    },
    "pad_thai": {
        "calories_per_100g": 170,
        "serving_size": 350,
        "description": "1 plate of Pad Thai (350g)",
        "protein": 8.0,
        "fat": 7.0,
        "carbs": 25.0,
        "suggestion": "Delicious noodles, but contain high amounts of sugar in tamarind sauce. Add bean sprouts and peanut garnish."
    },
    "paella": {
        "calories_per_100g": 156,
        "serving_size": 350,
        "description": "1 serving of Seafood Paella (350g)",
        "protein": 10.0,
        "fat": 5.0,
        "carbs": 18.0,
        "suggestion": "Seafood rice rich in iron, zinc, and protein. Watch rice portions to manage total carbohydrates."
    },
    "pancakes": {
        "calories_per_100g": 227,
        "serving_size": 150,
        "description": "3 Pancakes (150g)",
        "protein": 6.0,
        "fat": 6.0,
        "carbs": 37.0,
        "suggestion": "Fluffy breakfast food. Maple syrup and butter drastically raise sugar and calorie levels."
    },
    "panna_cotta": {
        "calories_per_100g": 280,
        "serving_size": 120,
        "description": "1 cup of Panna Cotta (120g)",
        "protein": 3.0,
        "fat": 22.0,
        "carbs": 18.0,
        "suggestion": "Creamy Italian dessert. High in saturated fat and dairy sugars. Eat occasionally."
    },
    "peking_duck": {
        "calories_per_100g": 337,
        "serving_size": 180,
        "description": "1 portion of Peking Duck (180g)",
        "protein": 19.0,
        "fat": 28.0,
        "carbs": 1.5,
        "suggestion": "A luxury dish rich in iron and protein. Duck skin is very fat-dense. Wrap in thin flour pancakes."
    },
    "pho": {
        "calories_per_100g": 85,
        "serving_size": 500,
        "description": "1 large bowl of Beef Pho (500g)",
        "protein": 6.0,
        "fat": 2.0,
        "carbs": 11.0,
        "suggestion": "A relatively low-fat Vietnamese noodle soup. High in sodium but rich in aromatic spices."
    },
    "pork_chop": {
        "calories_per_100g": 240,
        "serving_size": 180,
        "description": "1 grilled Pork Chop (180g)",
        "protein": 25.0,
        "fat": 15.0,
        "carbs": 0.0,
        "suggestion": "A good lean protein source that supplies thiamine (vitamin B1). Bake or grill to reduce fat."
    },
    "poutine": {
        "calories_per_100g": 270,
        "serving_size": 300,
        "description": "1 portion of Poutine (300g)",
        "protein": 9.0,
        "fat": 15.0,
        "carbs": 24.0,
        "suggestion": "French fries, cheese curds, and brown gravy. Very high in fats, carbs, and sodium. Treat as occasional indulgence."
    },
    "prime_rib": {
        "calories_per_100g": 300,
        "serving_size": 250,
        "description": "1 prime rib cut (250g)",
        "protein": 22.0,
        "fat": 24.0,
        "carbs": 0.0,
        "suggestion": "Savory beef cut rich in proteins and iron, but carries substantial marbled fat. Limit portion."
    },
    "bread_pudding": {
        "calories_per_100g": 270,
        "serving_size": 150,
        "description": "1 serving of Bread Pudding (150g)",
        "protein": 5.0,
        "fat": 11.0,
        "carbs": 38.0,
        "suggestion": "Traditional sweet baked pudding. High in simple carbs."
    },
    "pulled_pork_sandwich": {
        "calories_per_100g": 240,
        "serving_size": 200,
        "description": "1 Pulled Pork Sandwich (200g)",
        "protein": 18.0,
        "fat": 9.0,
        "carbs": 22.0,
        "suggestion": "Pork is high in protein, but sweet barbecue sauce increases sugar and calorie counts."
    },
    "ramen": {
        "calories_per_100g": 100,
        "serving_size": 450,
        "description": "1 bowl of Tonkotsu Ramen (450g)",
        "protein": 5.5,
        "fat": 4.5,
        "carbs": 10.0,
        "suggestion": "Comforting noodle soup, but pork bone broth can be high in saturated fat. Extremely high in sodium."
    },
    "ravioli": {
        "calories_per_100g": 200,
        "serving_size": 220,
        "description": "1 plate of cheese Ravioli (220g)",
        "protein": 8.0,
        "fat": 6.5,
        "carbs": 28.0,
        "suggestion": "Pasta stuffed with cheese or spinach. Moderate in protein. Avoid calorie-heavy butter or cream sauces."
    },
    "red_velvet_cake": {
        "calories_per_100g": 367,
        "serving_size": 120,
        "description": "1 slice of Red Velvet (120g)",
        "protein": 4.0,
        "fat": 17.0,
        "carbs": 49.0,
        "suggestion": "Very high in fats and sugars. Cream cheese frosting adds saturated fat. Enjoy in small slices."
    },
    "risotto": {
        "calories_per_100g": 160,
        "serving_size": 250,
        "description": "1 bowl of Mushroom Risotto (250g)",
        "protein": 4.0,
        "fat": 5.0,
        "carbs": 25.0,
        "suggestion": "Creamy Italian rice dish containing parmesan and butter. High in fast carbs."
    },
    "samosa": {
        "calories_per_100g": 262,
        "serving_size": 100,
        "description": "2 pieces of Samosa (100g)",
        "protein": 4.5,
        "fat": 12.0,
        "carbs": 33.0,
        "suggestion": "Deep-fried appetizer filled with potatoes and peas. High in trans-fats and simple carbs."
    },
    "sashimi": {
        "calories_per_100g": 120,
        "serving_size": 120,
        "description": "8 slices of Salmon/Tuna Sashimi (120g)",
        "protein": 22.0,
        "fat": 3.0,
        "carbs": 0.0,
        "suggestion": "Incredible high-protein, low-calorie dish. Full of healthy Omega-3 fatty acids. Best choice."
    },
    "scallops": {
        "calories_per_100g": 111,
        "serving_size": 150,
        "description": "5 seared Scallops (150g)",
        "protein": 20.0,
        "fat": 1.5,
        "carbs": 4.0,
        "suggestion": "Excellent source of high-quality lean protein, low in fat. Cook with light oil/butter."
    },
    "seaweed_salad": {
        "calories_per_100g": 70,
        "serving_size": 100,
        "description": "1 cup of Seaweed Salad (100g)",
        "protein": 1.5,
        "fat": 3.5,
        "carbs": 8.0,
        "suggestion": "Excellent source of minerals (iodine, calcium) and fiber. Sesame oil adds a small amount of healthy fats."
    },
    "shrimp_and_grits": {
        "calories_per_100g": 160,
        "serving_size": 300,
        "description": "1 plate of Shrimp & Grits (300g)",
        "protein": 12.0,
        "fat": 8.0,
        "carbs": 11.0,
        "suggestion": "Good protein from shrimp. Grits are corn-based and are often prepared with high cream and cheese."
    },
    "breakfast_burrito": {
        "calories_per_100g": 240,
        "serving_size": 220,
        "description": "1 Breakfast Burrito (220g)",
        "protein": 11.0,
        "fat": 12.0,
        "carbs": 22.0,
        "suggestion": "Provides high energy and protein (eggs, cheese, bacon). High in sodium and carbohydrates."
    },
    "spaghetti_bolognese": {
        "calories_per_100g": 130,
        "serving_size": 350,
        "description": "1 plate of Spaghetti Bolognese (350g)",
        "protein": 8.0,
        "fat": 4.5,
        "carbs": 15.0,
        "suggestion": "A classic Italian pasta meal. Watch noodles portions and choose lean ground beef for better health."
    },
    "spaghetti_carbonara": {
        "calories_per_100g": 220,
        "serving_size": 350,
        "description": "1 plate of Spaghetti Carbonara (350g)",
        "protein": 9.5,
        "fat": 12.0,
        "carbs": 18.0,
        "suggestion": "Pasta with egg yolks, cheese, and pancetta bacon. High in fats, calories, and sodium."
    },
    "spring_rolls": {
        "calories_per_100g": 250,
        "serving_size": 120,
        "description": "3 fried Spring Rolls (120g)",
        "protein": 4.0,
        "fat": 11.0,
        "carbs": 33.0,
        "suggestion": "Deep-fried rolls. Steamed rice paper summer rolls are a much healthier, lower-fat alternative."
    },
    "steak": {
        "calories_per_100g": 271,
        "serving_size": 200,
        "description": "1 Ribeye Steak (200g)",
        "protein": 25.0,
        "fat": 19.0,
        "carbs": 0.0,
        "suggestion": "Protein-dense and loaded with creatine, iron, and zinc. Pair with steamed greens instead of chips."
    },
    "strawberry_shortcake": {
        "calories_per_100g": 288,
        "serving_size": 150,
        "description": "1 slice of Strawberry Shortcake (150g)",
        "protein": 4.0,
        "fat": 15.0,
        "carbs": 34.0,
        "suggestion": "Provides strawberries, but whipped cream and sponge cake carry sugar and fat."
    },
    "sushi": {
        "calories_per_100g": 143,
        "serving_size": 150,
        "description": "6 pieces of Sushi Rolls (150g)",
        "protein": 6.0,
        "fat": 2.0,
        "carbs": 25.0,
        "suggestion": "A balanced, clean meal. Watch out for deep-fried tempura rolls or heavy mayonnaise toppings."
    },
    "tacos": {
        "calories_per_100g": 226,
        "serving_size": 180,
        "description": "2 Beef Tacos (180g)",
        "protein": 11.5,
        "fat": 11.0,
        "carbs": 20.0,
        "suggestion": "High protein. Hard shells are fried; soft corn tortillas are a healthier, lower fat choice."
    },
    "takoyaki": {
        "calories_per_100g": 180,
        "serving_size": 120,
        "description": "6 pieces of Octopus Balls (120g)",
        "protein": 6.0,
        "fat": 8.0,
        "carbs": 21.0,
        "suggestion": "Savory octopus pancake balls. High in carbohydrates and topped with salty sauces and mayonnaise."
    },
    "tiramisu": {
        "calories_per_100g": 354,
        "serving_size": 100,
        "description": "1 slice of Tiramisu (100g)",
        "protein": 5.0,
        "fat": 22.0,
        "carbs": 34.0,
        "suggestion": "Coffee-flavored dessert containing mascarpone cream, egg yolks, and ladyfingers. High in fat."
    },
    "tuna_tartare": {
        "calories_per_100g": 140,
        "serving_size": 100,
        "description": "1 portion of Tuna Tartare (100g)",
        "protein": 22.0,
        "fat": 5.0,
        "carbs": 2.0,
        "suggestion": "Excellent clean appetizer. Filled with protein and healthy monounsaturated fats from avocado and sesame."
    },
    "waffles": {
        "calories_per_100g": 290,
        "serving_size": 120,
        "description": "1 large Waffle (120g)",
        "protein": 6.0,
        "fat": 12.0,
        "carbs": 39.0,
        "suggestion": "Sweet carb-heavy breakfast. Minimize butter and sugary syrups, and choose fruit toppings."
    },
    "cannoli": {
        "calories_per_100g": 339,
        "serving_size": 90,
        "description": "1 large Cannoli (90g)",
        "protein": 5.0,
        "fat": 18.0,
        "carbs": 39.0,
        "suggestion": "Sweet Italian fried shell with ricotta filling. High in sugar and fats. Limit portion size."
    }
}
