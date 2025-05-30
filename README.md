# APPI - Adult Plant Projection Imaging

[![License](https://github.com/micropolimi/APPI/raw/main/images/licence_img.svg)](https://github.com/micropolimi/APPI/raw/main/LICENSE)

🚀 **Open Software & Hardware for Plant Imaging**

---

## 🌱 Overview
APPI (Adult Plant Projection Imaging) is an open-source project dedicated to advanced imaging of growing plants. It provides tools for:
✅ Software-controlled optical imaging using cameras and LEDs.
✅ Automated data analysis with region-of-interest (ROI) registration.
✅ Hardware integration for multiview plant growth monitoring.

<img src="https://github.com/micropolimi/APPI/raw/main/images/setup_total.jpg" width="300">
---

## 🖥️ Software Installation
The control software for APPI is based on [Scope Foundry]. To set up the python environment and install the software:
1. Follow the [Scope Foundry installation] guidelines.
2. Download or clone the [APPI code], which runs cameras, LEDs, and controls triggers with a dedicated [App].

---

## ⚙️ Software Usage
By running the *plant_app* script, a new window appears on the screen, allowing control of the APPI system. All acquisition parameters can be configured through the *Console* widget, located above the canvas. A detailed description of the options offered by the *Console* is provided below.

![software GUI](https://github.com/micropolimi/APPI/raw/main/images/APPI_GUI.png)

1) **Time Lapse Number**: Number of time points to be acquired.
2) **Waiting Time**: Time interval between consecutive time points.
3) **X - Y LED**: When not measuring, ticking the checkbox toggles the selected LED on or off. Facilitates accurate positioning of the sample prior to measurement. 
4) **View**: Enables switching from one view to another.
5) **Acquisition Time**: Exposure time. Use 4) to select the appropriate channel and set the exposure time. Exposure time may differ between channels X and Y.
6) **AutoRange** and **AutoLevels**: When unchecked, these boxes allow the user to manually define the displayed portion of the Field of View and and set the grayscale level limits.
7) **Save H5**: When this checkbox is checked, pressing the Start button will save a new acquisition. 
8) **Start** and **Interrupt**: These two buttons start and stop the measurment respectively.
9) **Save Dr**: Directory where data will be saved.
10) **Sample**: Name of the file to be saved.
11) **State bar**: Displays the percentage of completed acquisitions.

---

## 📊 Data Analysis
For analyzing APPI datasets of growing plants, we recommend using the [napari ROI Registration plugin]. This plugin is specifically designed for time-lapse registration of regions-of-interest.

![napari ROI Registration](https://github.com/micropolimi/APPI/raw/main/images/roi_registration.gif)

🔹 _Provides precise region tracking over time._   
🔹 _Easy-to-use with napari interface._

---

## 🛠️ Hardware Components
🚧 _Work in progress._

---

## 🏗️ Hardware Installation
🚧 _Work in progress._

---

## 🍃 Case study
🚧 _Work in progress._ Stay tuned for updates!

---

## 🔓 License

Distributed under the terms of the [BSD-3] license,
the APPI code is free and open source software

---

## 📬 Contribute & Support
Have suggestions or issues? Feel free to [file an issue] or contribute to the project!

🔗 **Useful Links:**
- [Scope Foundry] - Imaging framework
- [Scope Foundry Installation] - Step-by-step setup guide
- [APPI Code] - Source files
- [napari ROI Registration Plugin] - Data analysis tool

[Scope Foundry]: https://scopefoundry.org/
[Scope Foundry installation]: https://scopefoundry.org/docs/1_getting-started/
[file an issue]: https://github.com/micropolimi/APPI/issues
[Appi code]: https://github.com/micropolimi/APPI/raw/main/src
[App]: https://github.com/micropolimi/APPI/raw/main/src/plant_app.py
[napari Roi Registration plugin]: https://www.napari-hub.org/plugins/napari-roi-registration
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause