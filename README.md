# Vision-Flow: AI Traffic Intelligence

A Smart City simulation integrating **Computer Vision** with **Embedded Logic** to optimize traffic signals based on real-time density.

## Tech Stack
* **Logic:** C++ (State Machine)
* [cite_start]**Vision:** Python (YOLOv8, OpenCV) [cite: 26]
* [cite_start]**Dashboard:** Flask (Web UI) 
* **Comm:** UDP Sockets

## Quick Start
1. **Setup Environment:**
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate | Linux: source venv/bin/activate
   pip install -r requirements.txt

2. **Compile Controller** : g++ controller.cpp -o controller

3. **Run System (3 Terminals):**

        Term 1: ./controller (C++ Logic)

        Term 2: python app.py (Flask Dashboard)

        Term 3: python vision.py (AI Perception)

Project Structure

    vision.py: Vehicle detection & UDP data streaming. 

    controller.cpp: Real-time traffic logic & timing control. 

    app.py: Flask web dashboard for monitoring (Port 8080). 

    requirements.txt: Project dependencies (ultralytics, opencv-python, flask).