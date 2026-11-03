"""Проверка арифметики сценария Changellenge Cup Russia 2026.

Это учебная финансовая модель, не факт привлечения пайщиков.
"""

current = 6862
organic_per_year = 2581
years = 3
target = 22873
potential_audience = 105262

without_initiatives = current + years * organic_per_year
incremental_needed = target - without_initiatives
required_conversion = incremental_needed / potential_audience

annual_budget_mln = {
    "content": 7.5,
    "targeting": 30.0,
    "integrations": 14.0,
    "crm": 7.0,
    "bonuses": 7.0,
    "analytics": 4.5,
}
annual_total = sum(annual_budget_mln.values())
roadmap_additional = [2000, 3000, 3500]
planned_total = sum(roadmap_additional)
three_year_budget_rub = annual_total * 1_000_000 * years

assert without_initiatives == 14605
assert incremental_needed == 8268
assert round(annual_total, 2) == 70.0

print(f"Базовый прогноз без инициатив: {without_initiatives:,}".replace(",", " "))
print(f"Необходимый прирост: {incremental_needed:,}".replace(",", " "))
print(f"Требуемая конверсия за 3 года: {required_conversion:.2%}")
print(f"Ежегодный бюджет, млн руб.: {annual_total:,.1f}")
print(f"Плановый прирост roadmap: {planned_total:,}".replace(",", " "))
print(f"Превышение над расчётным разрывом: {planned_total - incremental_needed}")
print(f"Бюджет за 3 года, млн руб.: {three_year_budget_rub / 1e6:.0f}")
print(
    "Условные затраты на одного дополнительного пайщика, руб.: "
    f"{three_year_budget_rub / incremental_needed:,.0f}".replace(",", " ")
)
