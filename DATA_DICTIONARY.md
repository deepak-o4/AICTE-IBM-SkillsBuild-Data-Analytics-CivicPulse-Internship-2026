# CivicPulse Data Dictionary

## Source data columns
The BBMP grievance dataset comprises the following fields:

| Column | Description |
|---|---|
| Complaint ID | Unique identifier for each complaint record |
| Category | Primary civic complaint category |
| Sub Category | More granular subcategory under the parent complaint group |
| Grievance Date | Complaint registration timestamp |
| Ward Name | Bengaluru ward associated with the complaint |
| Grievance Status | Action status of the complaint record |
| Staff Remarks | Notes provided by municipal staff |
| Staff Name | Officer or staff member assigned/recorded |

## Derived columns
The following fields are created during processing:

| Column | Description |
|---|---|
| Year | Calendar year extracted from Grievance Date |
| Month | Full month name |
| Quarter | Fiscal quarter (e.g., 2024Q1) |
| DayOfWeek | Day of complaint creation |

## Status values observed in the data
- Closed
- Rejected
- Non Relevant
- Registered
- Resolved
- ReOpen
- In Progress
- Long Term Solution
- Unknown

## Category coverage
The most frequent categories in the combined dataset are:
1. Electrical
2. Solid Waste (Garbage) Related
3. Road Maintenance(Engg)
4. Forest
5. Health Dept
6. Veterinary
7. Road Infrastructure
8. Others
9. Storm Water Drain(SWD)
10. Town Planning

## Notes on data quality
- Duplicate complaint IDs were removed during cleaning.
- Missing or invalid dates were dropped from the clean dataset.
- Empty or malformed text fields were standardized to "Unknown" when necessary.
