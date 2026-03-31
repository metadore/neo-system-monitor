# 🚀 Futuristic CPU Monitor

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white) 
![Rich](https://img.shields.io/badge/rich-1.13.0-pink?logo=python&logoColor=white) 
![License](https://img.shields.io/badge/license-MIT-green)

A **real-time, terminal-based CPU monitoring dashboard** built with Python, `psutil`, and `rich`.  
Monitor **CPU usage**, **per-core activity**, and **system stats** with a sleek, futuristic interface — all running in your terminal.  

---

## ✨ Features

- ⚡ **Real-time CPU Monitoring** – Smooth updates every 0.5 seconds  
- 🧠 **CPU Overview Panel** – Total usage, CPU frequency, and number of cores  
- 🎨 **Beautiful Terminal UI** – Panels, progress bars, and colors using `rich`  
- 🖥️ **Per-core Usage Visualization** – Dynamic progress bars for every CPU core  
- 🛠️ **Modular & Extendable** – Easily add RAM, GPU, disk, or network monitoring  

---

## 📸 Demo

![Demo Placeholder](https://via.placeholder.com/800x350.png?text=Replace+with+Your+GIF+or+Screenshot)  

*Replace this placeholder with a screenshot or GIF of the monitor running in your terminal for maximum effect.*  

---

## 🛠️ Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2.Install dependencies
pip install psutil rich
Run the monitor
python monitor.py
Exit
Press CTRL+C to stop the monitor.
💡 Learning Notes

This project was created during my first exploration of Linux system monitoring.
I combined AI-generated code with hands-on experimentation, customizing the UI and learning how to:

Collect real-time CPU data using psutil
Build dynamic terminal layouts with rich
Display per-core progress bars
Organize Python code in a modular and reusable structure

📝 Tip: Use this as a foundation to expand your dashboard with RAM, disk, network, or GPU metrics.

📂 Project Structure
futuristic-cpu-monitor/
│
├─ monitor.py          # Main script
├─ README.md           # Project documentation
├─ screenshots/        # Optional folder for preview images or GIFs
└─ requirements.txt    # Optional: dependencies
🔧 Future Enhancements
Add RAM, disk, and network monitoring
Include system temperature & fan speed
Make the monitor theme-switchable
Add logging mode to record CPU usage over time
Animate per-core usage in a GIF for a visually stunning demo
📝 License

This project is licensed under the MIT License – feel free to experiment and learn from it.

🌟 Conclusion

This dashboard is a hands-on showcase of Python and Linux experimentation, demonstrating how AI-assisted code combined with personal customization can help you build impressive terminal tools while learning real system-level programming skills.
