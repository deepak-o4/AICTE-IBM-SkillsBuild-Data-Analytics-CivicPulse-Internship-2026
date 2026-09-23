# CivicPulse Project Decisions

## Scope decision
This project focuses on historical BBMP grievance analytics rather than complaint-image or NLP-based citizen intelligence. It is explicitly aligned with the operational brief for a municipal trend and decision-support dashboard.

## Dataset decision
The project uses the available BBMP CSV files covering 2020–2024. The records are combined after schema validation and duplicate checks.

## Visual direction
The provided Gradient Able admin template was used as a visual reference for a clean, modern dashboard aesthetic. The final Streamlit dashboard retains the same overall administrative styling principles without duplicating proprietary template code.

## ML decision
A ward-level K-Means segmentation is included because the brief specifically mentions ward civic profile segmentation and this is supported by reliable ward-level features derived from the dataset.

## Reporting decision
The project uses real metrics from the cleaned dataset and documents the actual outputs generated during execution.
