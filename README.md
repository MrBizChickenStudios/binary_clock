# Binary Clock

A Python-based binary clock that simulates a real-time clock using binary digits represented by lights. The clock updates in real-time and shows hours, minutes, and seconds in binary format. It also includes flashing separators between the time components to visually represent the passage of time.

## Features

- **Real-Time Binary Clock**: Displays time in binary format using lights for hours, minutes, and seconds.
- **Flashing Separators**: Blinking lights act as separators between hours, minutes, and seconds.
- **Pygame-Based GUI**: A smooth graphical interface built using the Pygame library.
- **Customizable**: Easily adjust light colors, size, and screen dimensions through constants.

## Requirements

- Python 3.x
- Pygame library

### Installing Dependencies

Before running the project, ensure that you have Python 3.x installed. You can install the required dependencies using `pip`:

```bash
pip install pygame
Installation
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/binary-clock.git
cd binary-clock
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python main.py
How It Works
The clock displays the current time using binary lights for each digit in the time (hours, minutes, seconds). Each digit is represented by a set of lights, and their on/off states are determined by the corresponding binary value of the digit.

The lights for each time unit (hours, minutes, seconds) are updated every second.
Flashing separators between the time units (hours:minutes:seconds) are represented by separate lights that blink at a regular interval.
Project Structure
The project consists of the following main components:

clock.py: Contains the logic for the clock, including the update and display of the time in binary format.
light.py: Handles the creation and management of the lights that represent the binary digits and separators.
main.py: The main entry point for the program, handling the Pygame loop, updating, and drawing the clock.
constants.py: Defines the constants used in the project, such as screen dimensions, padding, and colors.
Usage
Run the clock: After installation, simply run the program by executing python main.py from the command line. The binary clock will appear with the current time in binary format.
Customizing the Clock: You can adjust the appearance of the clock (like the size of the lights or the clock dimensions) by editing the constants defined in constants.py.
Flashing Separators: The separators between hours, minutes, and seconds will automatically flash on and off every 1.5 seconds, simulating the visual separation between these time components.
Example
The clock displays time in a binary format, such as:

yaml
Copy
Edit
Hours: 15 -> 1111
Minutes: 53 -> 110101
Seconds: 30 -> 11110
Contributions
Feel free to fork the repository and submit pull requests. If you encounter any bugs or want to suggest features, please open an issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet
Copy
Edit

Now you can copy the entire block and paste it directly into your `README.md` on GitHub! Let me know if you need any further modifications.






