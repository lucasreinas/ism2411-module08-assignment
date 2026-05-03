# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Services dictionary
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Consulting": 200,
    "Cybersecurity": 220,
    "IT Support": 90
}

# TODO 2: Customer dictionaries
customer1 = {
    "company_name": "TechNova Inc",
    "contact_person": "Alice Smith",
    "email": "alice@technova.com",
    "phone": "813-555-1111"
}

customer2 = {
    "company_name": "BrightPath LLC",
    "contact_person": "Brian Lee",
    "email": "brian@brightpath.com",
    "phone": "813-555-2222"
}

customer3 = {
    "company_name": "FutureWave Corp",
    "contact_person": "Carla Gomez",
    "email": "carla@futurewave.com",
    "phone": "813-555-3333"
}

customer4 = {
    "company_name": "NextGen Solutions",
    "contact_person": "David Chen",
    "email": "david@nextgen.com",
    "phone": "813-555-4444"
}

# TODO 3: Master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(cid, info)

# TODO 5: Lookups
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update info
customers["C001"]["phone"] = "813-555-9999"
customers["C002"]["industry"] = "Finance"

print("\nUpdating Customer Information:")
print("-" * 60)
for cid, info in customers.items():
    print(cid, info)

# TODO 7: Project dictionaries
projects = {
    "C001": [
        {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000},
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 40, "budget": 9000}
    ],
    "C002": [
        {"name": "Sales Dashboard", "service": "Data Analysis", "hours": 60, "budget": 10500}
    ],
    "C003": [
        {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 80, "budget": 16000}
    ],
    "C004": []
}

print("\nProject Information:")
print("-" * 60)
for cid, plist in projects.items():
    print(cid, plist)

# TODO 8: Project cost calculations
print("\nProject Cost Calculations:")
print("-" * 60)
for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(p["name"], "Cost:", cost)

# TODO 9: Dictionary methods
print("\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", customers.keys())
companies = [c["company_name"] for c in customers.values()]
print("Companies:", companies)
print("Total Customers:", len(customers))

# TODO 10: Service usage
service_counts = {}

for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
all_projects = [p for plist in projects.values() for p in plist]

total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(p["budget"] for p in all_projects)
min_budget = min(p["budget"] for p in all_projects)

print("\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary
print("\nCustomer Summary Report:")
print("-" * 60)
for cid, info in customers.items():

    cust_projects = projects.get(cid, [])
    total_hours_c = sum(p["hours"] for p in cust_projects)
    total_budget_c = sum(p["budget"] for p in cust_projects)

    print(info["company_name"])
    print("Projects:", len(cust_projects))
    print("Hours:", total_hours_c)
    print("Budget:", total_budget_c)
    print()

# TODO 13: Rate adjustments
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\nAdjusted Service Rates:")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Active customers
active_customers = {cid: customers[cid] for cid, plist in projects.items() if len(plist) > 0}

print("\nActive Customers:")
print("-" * 60)
print(active_customers)

# TODO 15: Customer budget totals
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print("\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service tiers
service_tiers = {
    service: (
        "Premium" if rate >= 200 else
        "Standard" if rate >= 100 else
        "Basic"
    )
    for service, rate in services.items()
}

print("\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation
def validate_customer(customer_dict):

    required = ["company_name", "contact_person", "email", "phone"]

    for field in required:
        if field not in customer_dict:
            return False

    return True


print("\nCustomer Validation:")
print("-" * 60)
for cid, info in customers.items():
    print(cid, validate_customer(info))

# TODO 18: Project status tracking
status_counts = {"active": 0, "completed": 0, "pending": 0}

for plist in projects.values():
    for p in plist:
        p["status"] = "active"
        status_counts["active"] += 1

print("\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function
def analyze_customer_budgets(projects_dict):

    results = {}

    for cid, plist in projects_dict.items():

        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count > 0 else 0

        results[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return results


print("\nDetailed Budget Analysis:")
print("-" * 60)

analysis = analyze_customer_budgets(projects)
print(analysis)

# TODO 20: Service recommendation
def recommend_services(customer_id, customers, projects, services):

    used_services = {p["service"] for p in projects.get(customer_id, [])}

    recommendations = []

    for service in services:
        if service not in used_services:
            recommendations.append(service)

    return recommendations


print("\nService Recommendations:")
print("-" * 60)

for cid in customers:
    recs = recommend_services(cid, customers, projects, services)
    print(cid, recs)