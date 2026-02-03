# Luxury Car Sales & Market Analyzer v1.0
# Developed by: Hussein Younes (hjy11595)
# Expertise: 8.5+ Years in Sales & Marketing (LIU Graduate)

def analyze_car_deal(car_model, price, demand_level):
    """
    تحليل احتمالية نجاح الصفقة بناءً على خبرة حسين الميدانية
    """
    print(f"--- Analyzing Deal for: {car_model} ---")
    
    # خوارزمية بسيطة لتقييم الصفقة (Lead Scoring)
    score = 0
    if demand_level.lower() == "high":
        score += 50
    if price < 500000: # مثال لسعر سيارة فاخرة
        score += 30
    else:
        score += 15
        
    print(f"Market Success Probability: {score}%")
    
    if score > 70:
        return "Recommendation: HIGH PRIORITY - Close the deal immediately!"
    else:
        return "Recommendation: Follow up with marketing automation."

# تجربة الأداة
result = analyze_car_deal("Lamborghini Huracan", 450000, "high")
print(result)

