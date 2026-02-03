# General Sales & Marketing Opportunity Analyzer
# Hussein Younes | 8.5+ Years Experience | Marketing Graduate (LIU)

def analyze_job_offer(company_rank, salary_package, industry):
    """
    تقييم العرض الوظيفي بناءً على معايير حسين المهنية
    """
    score = 0
    if company_rank == "Top Tier": score += 40
    if salary_package == "Strong": score += 40
    
    print(f"Analyzing offer from {industry} sector...")
    
    if score >= 80:
        return "Verdict: Strong Opportunity. Apply immediately!"
    else:
        return "Verdict: Evaluate based on long-term career growth."

# تجربة الكود لقطاعات مختلفة (عقارات، تكنولوجيا، سيارات)
print(analyze_job_offer("Top Tier", "Strong", "Real Estate/Retail"))
