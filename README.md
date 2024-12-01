# 🏋️ Gym Progress Tracker

A Python-based tool to visualize the maximum weight progress for each exercise performed in the gym. The script processes data from a CSV file and generates insightful graphs to help track weight progress over time. 📊

---

## ✨ Features
- 📂 Parse CSV files containing gym workout data.  
- 📈 Generate graphs showing the trend of the maximum weight for each exercise.  
- 💾 Export graphs in jpg formato.  
- 🔧 Easily customizable for additional analysis.  

---
## ⚠️ Attention
The script is actualy only able to analize CVS from [Hevy](https://hevy.com).
If you use Docker pay attention cause the container is builded with charts images inside, so if you consider your workout data sensible do not push it to a registry.

---

## ⚙️ Prerequisites
- 🐍 Python 3.8+  
- Required Python libraries (see `requirements.txt`)  

---

## 🚀 Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/Reda2200/workout-chart.git 
   cd gym-progress-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **CSV file**:
    This script generate chart starting from csv file of your workout extracted from [Hevy](https://hevy.com). To Download the file follow this step:
    
    - log in to your account at [hevy.com](https://hevy.com)
    - go to Setting ➡️ Export Data ➡️ Click on "Export Workout Data"
    
    Copy the file in the same Directory of the script.
    #####
    ###### Feel free to download the code and modify it to fit your data
    #####
    
4. **Run the script**:
   ```bash
   python3 main.py
   ```

---

## 🐳 Using Docker

This project include a Docker integration for a better experience. 🚀
whit this docker conatainer you can see your chart at ```<IP-OF-YOUR-SERVER>:4321```

### 📦 Build the Docker Image
1. Ensure Docker is installed and running.
2.  Remember to copy the CSV file in the same directory where you clone this repo
3. Build the Docker image:
   ```bash
   docker build -t gym-chart .
   ```

### ▶️ Run the Container

To execute the script using Docker:
```bash
docker run --name gym-chart
```    

### 🛠️ Dockerfile Overview
The ```Dockerfile``` include web server using the template [Astro Multiverse](https://github.com/AREA44/astro-multiverse) Created by [AREA44](https://github.com/AREA44). The web page is reachable at the port ```4321``` of your server

---
## 🤝 Contributing

Contributions are welcome! 🧑‍💻 Feel free to open issues, suggest features, or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License. See the ```LICENSE``` file for more details.

---

## 🙏 Acknowledgments

Special thanks to [AREA44](https://github.com/AREA44) for the template [Astro Multiverse](https://github.com/AREA44/astro-multiverse).

---

## 🔮 Future implementation

- [ ] Add Docker Compose
- [ ] Add Dropset and failture set in the chart
- [ ] Create a Docker image throgh gitflow 
- [ ] Trigger python script at first container start
- [ ] Schedule crontab to update charts at last data
- [ ] Implement Selenium to automaticaly download workout data