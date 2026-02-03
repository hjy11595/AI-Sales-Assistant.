# متطور لتقدير أسعار تأجير السيارات الفاخرة AI نموذج 
# مخصص لـ hjy11595 - خبير مبيعات وتسويق

def calculate_luxury_price(model, days, is_vip=False):
    prices = {
        "lamborghini": 4000,
        "ferrari": 3800,
        "rolls_royce": 4500,
        "mercedes_g63": 2500
    }
    
    # السعر الأساسي
    base_rate = prices.get(model.lower(), 1500)
    total = base_rate * days
    
    # خصم ذكي للسيلز: إذا كانت المدة أكثر من 5 أيام
    if days > 5:
        total *= 0.85  # خصم 15%
        
    # معاملة الـ VIP (إضافة تسويقية)
    if is_vip:
        total *= 0.95  # خصم إضافي للـ VIP
        
    return f"Car: {model.upper()} | Quote for {days} days: {total} AED/QAR"

# تجربة الكود لعميل VIP يريد استئجار لامبورجيني لمدة 7 أيام
print(calculate_luxury_price("lamborghini", 7, is_vip=True))

