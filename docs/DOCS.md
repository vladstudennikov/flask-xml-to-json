# Software Specification: XML <=> JSON Converter

## 1. Introduction

This document provides a detailed specification for the XML <=> JSON Converter project. This web-based tool allows users to convert data between XML and JSON formats. The application is designed with a client-server architecture, featuring a user-friendly web interface and a robust backend server.

## 2. Scope

The scope of this project is to provide a simple and efficient tool for converting data between XML and JSON formats, specifically for a predefined data structure representing personal information.

### In Scope:
-   Conversion of XML data to JSON data.
-   Conversion of JSON data to XML data.
-   A web-based user interface for easy interaction with the conversion tool.
-   Support for a specific data model (`FullPersonalData`).

### Out of Scope:
-   Support for arbitrary XML or JSON structures.
-   User authentication or data storage.
-   Advanced error handling or validation beyond basic format checking.
-   A command-line interface (CLI).

## 3. Functional Requirements

### 3.1. XML to JSON Conversion
-   **FR-001**: The system shall accept XML data as input from the user.
-   **FR-002**: The system shall convert the provided XML data into the equivalent JSON format.
-   **FR-003**: The system shall display the resulting JSON data to the user.

### 3.2. JSON to XML Conversion
-   **FR-004**: The system shall accept JSON data as input from the user.
-   **FR-005**: The system shall convert the provided JSON data into the equivalent XML format.
-   **FR-006**: The system shall display the resulting XML data to the user.

### 3.3. User Interface
-   **FR-007**: The user interface shall provide separate input fields for XML and JSON data.
-   **FR-008**: The user interface shall provide buttons to trigger the conversion process.
-   **FR-009**: The user interface shall display the output of the conversion in a read-only field.
-   **FR-010**: The user interface shall provide a button to copy the output to the clipboard.

## 4. Non-Functional Requirements

### 4.1. Performance
-   **NFR-001**: The conversion process should be completed within 2 seconds for typical data sizes (up to 1MB).
-   **NFR-002**: The web interface should load in under 3 seconds on a standard broadband connection.

### 4.2. Usability
-   **NFR-003**: The user interface should be intuitive and easy to use, even for non-technical users.
-   **NFR-004**: The application should be responsive and accessible on modern web browsers (Chrome, Firefox, Safari, Edge).

### 4.3. Reliability
-   **NFR-005**: The server should be available 99.9% of the time.
-   **NFR-006**: The application should handle invalid input gracefully and provide meaningful error messages.

### 4.4. Maintainability
-   **NFR-007**: The code should be well-structured, commented, and easy to understand.
-   **NFR-008**: The project should include a clear dependency list (`requirements.txt`).

## 5. System Architecture

The system is based on a client-server architecture.

### 5.1. Client (Frontend)
-   **Technology**: HTML, CSS, JavaScript, Bootstrap
-   **Structure**: A single-page application that communicates with the backend via asynchronous HTTP requests (AJAX).
-   **Components**:
    -   `index.html`: The main structure of the web page.
    -   `styles.css`: Custom styles for the user interface.
    -   `script.js`: Handles user interactions and communication with the backend.

### 5.2. Server (Backend)
-   **Technology**: Python, Flask
-   **Structure**: A Flask web server that exposes a RESTful API.
-   **Endpoints**:
    -   `POST /xml-to-json`: Accepts XML data and returns JSON.
    -   `POST /json-to-xml`: Accepts JSON data and returns XML.
-   **Modules**:
    -   `main.py`: The main entry point of the Flask application.
    -   `personal_data.py`: Defines the data model and the conversion logic (pure Python).
    -   `main_with_libs.py`: An alternative entry point that uses a library-based approach for conversion.
    -   `personal_data_libs.py`: A version of the data model that uses `dataclasses` and the `xmltodict` library.

## 6. Data Model

The application uses a predefined data model to represent personal information.

### 6.1. `PersonalData`
-   `name` (string)
-   `surname` (string)
-   `email` (string)

### 6.2. `Address`
-   `country` (string)
-   `region` (string)
-   `town` (string)
-   `street` (string)

### 6.3. `Work`
-   `company` (string)
-   `position` (string)
-   `education` (string)

### 6.4. `FullPersonalData`
-   `personal_data` (object of type `PersonalData`)
-   `address` (object of type `Address`)
-   `work` (object of type `Work`)

This structure is used for both XML and JSON data, with the root element in XML being `<root>`.
