# Online Resume Platform - Software Requirements Specification (SRS)

## 1. Introduction
The Online Resume Platform is a web-based application that allows members to showcase their professional profiles, including skills, experience, and education. It also fosters a community by allowing members to provide feedback through a rating system.

## 2. Functional Requirements

### 2.1 Member Profile Management
- **Create/Update Resume**: Members shall be able to create and update their professional resume.
- **Success Highlights**: Members can list their major professional achievements.
- **Skills**: Members can list and manage their technical and soft skills.
- **Previous Job**: Members can document their work history, including company, position, and dates.
- **Education**: Members can list their educational background.
- **Profile Image**: Members can upload and update a professional profile picture.

### 2.2 Resume Discovery and Interaction
- **Browse Resumes**: Any member can view the resumes of other members.
- **Rating System**: Members can rate other's resumes on a scale (e.g., 1-5 stars).
- **Average Rating**: The platform shall display the average rating for each resume.

## 3. Data Requirements
- **User**: Standard authentication details.
- **Resume**: Linked to User, contains success summary and profile image.
- **Skill**: A list of skills that can be associated with resumes.
- **PreviousJob**: Includes Company name, position, start/end dates, and description.
- **Education**: Includes School name, degree, and graduation year.
- **Rating**: Stores the score given by one user to another's resume.

## 4. UI/UX Requirements
- **Responsive Design**: The platform must be accessible on both desktop and mobile devices.
- **Modern Interface**: A clean, professional look and feel suitable for a career platform.
- **Interactive Rating**: A smooth UI for selecting and submitting ratings.

---
*Note: This document serves as the primary requirement guide for the development of the Online Resume Platform.*
