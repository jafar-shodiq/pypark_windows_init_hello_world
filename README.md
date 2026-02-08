# PySpark Exploration Project (BRI)

This repository contains a PySpark development environment configured for Windows. It is optimized to avoid common local execution errors like the `EOFException` and `winutils` pathing issues.

---

## 🛠 System Requirements

To run this project on Windows, you must have the following installed:

* **Java**: [JDK 17 (Temurin)](https://adoptium.net/temurin/releases/?version=17) or [JDK 11](https://adoptium.net/temurin/releases/?version=11).
* **Python**: **3.11.x** (Required).
    * *Note: Python 3.12+ is currently unstable with PySpark on Windows and causes worker crashes.*
* **Package Manager**: [uv](https://docs.astral.sh/uv/) for environment and dependency management.

---

## ⚙️ Environment Configuration

### 1. Hadoop Winutils Setup
Spark requires `winutils.exe` to simulate Linux-style file permissions on Windows.

1.  Create a folder: `C:\hadoop\bin`.
2.  Place `winutils.exe` inside that `bin` folder.
3.  Open **Environment Variables** in Windows and add:
    * **Variable Name**: `HADOOP_HOME`
    * **Variable Value**: `C:\hadoop`
4.  Edit the **Path** variable and add: `%HADOOP_HOME%\bin`.

### 2. Java Home
Ensure `JAVA_HOME` is set to your JDK installation path (e.g., `C:\Program Files\Eclipse Adoptium\jdk-17...`).

---

## 🚀 Getting Started

### 1. Initialize the Environment
Use `uv` to create a virtual environment specifically using Python 3.11:

```powershell
# Create venv with Python 3.11
uv venv --python 3.11

# Install dependencies
uv pip install pyspark

# Run
uv run python -m src.main