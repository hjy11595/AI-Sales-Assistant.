# نموذج بسيط لتحليل احتمالية نجاح الصفقة
def deal_probability(client_interest_level, budget_match):
    score = client_interest_level + budget_match
    return f"Deal Success Probability: {score}%"

# مثال: اهتمام عالي (50) وميزانية متناسبة (40)
print(deal_probability(50, 40))
