num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print("Total seconds in", num_years, "years:", total_secs)
total_days = num_years * days_per_year
print("Total days in", num_years, "years:", total_days)

# Question 4:
births_per_min = 250
births_per_day = births_per_min * mins_per_hour * hours_per_day

