# 🚗  Garage system


A command-line system for a car maintenance center. It opens the webcam, reads the
car's license plate (OCR), and then:

- **Plate already registered** → shows the vehicle, its service history and the upcoming maintenance.
- **Plate not registered** → asks for the owner and car details and saves them.

All data is stored in a JSON file (`data/vehicles.json`).

## Features
- Interactive CLI menu (arrow keys) with colored tables
- **Live** webcam scan using **Apple Vision** (built into macOS, Arabic + English): a box follows the plate and the number is captured automatically once it is stable, then the staff confirms it
- Switch between the Mac webcam and the iPhone camera with one key
- "Did you mean...?" suggestions when the OCR misreads a character
- Manual plate entry as a fallback (no camera / OCR mistakes / not on macOS)
- Service history and total cost per vehicle
- Automatic upcoming maintenance with status: `OK`, `SOON`, `OVERDUE`, `NO RECORD`
- Input validation (phone, year, mileage, cost) and error handling (no camera, corrupted JSON)
- Unit tests with pytest

## Requirements
- A recent Python 3 (3.11 or newer; works with the latest releases)
- macOS for automatic plate reading (other systems can still use manual entry)
- A webcam (optional)



## How to use the camera
Choose **Scan plate with camera**. The video is live and the program looks for a plate by itself:

1. Hold the plate in front of the camera. A **green box** appears around it.
2. When the same number is read 3 times in a row it is captured automatically.
3. Confirm the number (or correct it by hand), then the system shows the history or registers the car.



The chosen camera is remembered for the next run (`data/camera.json`).
Always check the detected plate before confirming; OCR can make mistakes.



## Maintenance rules
| Service    | Every                     |
|------------|---------------------------|
| Oil change | 5,000 km or 6 months      |
| Filters    | 10,000 km or 12 months    |
| Brakes     | 20,000 km                 |
| Tires      | 40,000 km                 |

A service is `OVERDUE` when the km or date limit is passed, and `SOON` when less than
500 km or 30 days remain. Rules can be edited in `SERVICE_RULES` inside `garage/service.py`.

