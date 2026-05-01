# AWS Scalable Flask App 🚀

## 📌 Overview

This project demonstrates deployment of a scalable web application using AWS services.

## 🏗️ Architecture

EC2 → Flask App → RDS (MySQL) → API → Internet
CI/CD via GitHub Actions

## 🔧 Tech Stack

* AWS EC2
* AWS RDS (MySQL)
* Application Load Balancer
* GitHub Actions (CI/CD)
* Python Flask

## 🔐 Security

* Used environment variables (no hardcoded credentials)
* Security Groups for controlled access

## 🚀 How to Run

1. Clone repo
2. Set environment variables:

   * DB_HOST
   * DB_USER
   * DB_PASSWORD
   * DB_NAME
3. Run:
   python3 app.py

## 📸 Demo

(Add screenshot of your app here)

## 📈 Key Learnings

* Cloud deployment & networking
* Debugging real-world infra issues
* CI/CD automation
