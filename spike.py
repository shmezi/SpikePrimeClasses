class Direction:
    Shortest_path = "Shortest path" #could run in either direction, depending on the shortest distance to the target.
    Clockwise = "Clockwise" #will make the motor run clockwise until it reaches the target position.
    Counterclockwise = "Counterclockwise" #will make the motor run counterclockwise until it reaches the target position.

class Sound:
    """
    Available predefined sounds provided by the spike hub.
    """
    Alert = "Alert"
    Applause_1 = "Applause 1"
    Applause_2 = "Applause 2"
    Applause_3 = "Applause 3"
    Baa = "Baa"
    Bang_1 = "Bang 1"
    Bang_2 = "Bang 2"
    Basketball_Bounce = "Basketball Bounce"
    Big_Boing = "Big Boing"
    Bird = "Bird"
    Bite = "Bite"
    Boat_Horn_1 = "Boat Horn 1"
    Boat_Horn_2 = "Boat Horn 2"
    Bonk = "Bonk"
    Boom_Cloud = "Boom Cloud"
    Boop_Bing_Bop = "Boop Bing Bop"
    Bowling_Strike = "Bowling Strike"
    Burp_1 = "Burp 1"
    Burp_2 = "Burp 2"
    Burp_3 = "Burp 3"
    Car_Accelerate_1 = "Car Accelerate 1"
    Car_Accelerating_2 = "Car Accelerating 2"
    Car_Horn = "Car Horn"
    Car_Idle = "Car Idle"
    Car_Reverse = "Car Reverse"
    Car_Skid_1 = "Car Skid 1"
    Car_Skid_2 = "Car Skid 2"
    Car_Vroom = "Car Vroom"
    Cat_Angry = "Cat Angry"
    Cat_Happy = "Cat Happy"
    Cat_Hiss = "Cat Hiss"
    Cat_Meow_1 = "Cat Meow 1"
    Cat_Meow_2 = "Cat Meow 2"
    Cat_Meow_3 = "Cat Meow 3"
    Cat_Purring = "Cat Purring"
    Cat_Whining = "Cat Whining"
    Chatter = "Chatter"
    Chirp = "Chirp"
    Clang = "Clang"
    Clock_Ticking = "Clock Ticking"
    Clown_Honk_1 = "Clown Honk 1"
    Clown_Honk_2 = "Clown Honk 2"
    Clown_Honk_3 = "Clown Honk 3"
    Coin = "Coin"
    Collect = "Collect"
    Connect = "Connect"
    Crank = "Crank"
    Crazy_Laugh = "Crazy Laugh"
    Croak = "Croak"
    Crowd_Gasp = "Crowd Gasp"
    Crunch = "Crunch"
    Cuckoo = "Cuckoo"
    Cymbal_Crash = "Cymbal Crash"
    Disconnect = "Disconnect"
    Dog_Bark_1 = "Dog Bark 1"
    Dog_Bark_2 = "Dog Bark 2"
    Dog_Bark_3 = "Dog Bark 3"
    Dog_Whining_1 = "Dog Whining 1"
    Dog_Whining_2 = "Dog Whining 2"
    Doorbell_1 = "Doorbell 1"
    Doorbell_2 = "Doorbell 2"
    Doorbell_3 = "Doorbell 3"
    Door_Closing = "Door Closing"
    Door_Creek_1 = "Door Creek 1"
    Door_Creek_2 = "Door Creek 2"
    Door_Handle = "Door Handle"
    Door_Knock = "Door Knock"
    Door_Slam_1 = "Door Slam 1"
    Door_Slam_2 = "Door Slam 2"
    Drum_Roll = "Drum Roll"
    Dun_Dun_Dunnn = "Dun Dun Dunnn"
    Emotional_Piano = "Emotional Piano"
    Fart_1 = "Fart 1"
    Fart_2 = "Fart 2"
    Fart_3 = "Fart 3"
    Footsteps = "Footsteps"
    Gallop = "Gallop"
    Glass_Breaking = "Glass Breaking"
    Glug = "Glug"
    Goal_Cheer = "Goal Cheer"
    Gong = "Gong"
    Growl = "Growl"
    Grunt = "Grunt"
    Hammer_Hit = "Hammer Hit"
    Head_Shake = "Head Shake"
    High_Whoosh = "High Whoosh"
    Jump = "Jump"
    Jungle_Frogs = "Jungle Frogs"
    Laser_1 = "Laser 1"
    Laser_2 = "Laser 2"
    Laser_3 = "Laser 3"
    Laughing_Baby_1 = "Laughing Baby 1"
    Laughing_Baby_2 = "Laughing Baby 2"
    Laughing_Boy = "Laughing Boy"
    Laughing_Crowd_1 = "Laughing Crowd 1"
    Laughing_Crowd_2 = "Laughing Crowd 2"
    Laughing_Girl = "Laughing Girl"
    Laughing_Male = "Laughing Male"
    Lose = "Lose"
    Low_Boing = "Low Boing"
    Low_Squeak = "Low Squeak"
    Low_Whoosh = "Low Whoosh"
    Magic_Spell = "Magic Spell"
    Male_Jump_1 = "Male Jump 1"
    Male_Jump_2 = "Male Jump 2"
    Moo = "Moo"
    Ocean_Wave = "Ocean Wave"
    Oops = "Oops"
    Orchestra_Tuning = "Orchestra Tuning"
    Party_Blower = "Party Blower"
    Pew = "Pew"
    Ping_Pong_Hit = "Ping Pong Hit"
    Plane_Flying_By = "Plane Flying By"
    Plane_Motor_Running = "Plane Motor Running"
    Plane_Starting = "Plane Starting"
    Pluck = "Pluck"
    Police_Siren_1 = "Police Siren 1"
    Police_Siren_2 = "Police Siren 2"
    Police_Siren_3 = "Police Siren 3"
    Punch = "Punch"
    Rain = "Rain"
    Ricochet = "Ricochet"
    Rimshot = "Rimshot"
    Ring_Tone = "Ring Tone"
    Rip = "Rip"
    Robot_1 = "Robot 1"
    Robot_2 = "Robot 2"
    Robot_3 = "Robot 3"
    Rocket_Explosion_Rumble = "Rocket Explosion Rumble"
    Rooster = "Rooster"
    Scrambling_Feet = "Scrambling Feet"
    Screech = "Screech"
    Seagulls = "Seagulls"
    Service_Announcement = "Service Announcement"
    Sewing_Machine = "Sewing Machine"
    Ship_Bell = "Ship Bell"
    Siren_Whistle = "Siren Whistle"
    Skid = "Skid"
    Slide_Whistle_1 = "Slide Whistle 1"
    Slide_Whistle_2 = "Slide Whistle 2"
    Sneaker_Squeak = "Sneaker Squeak"
    Snoring = "Snoring"
    Snort = "Snort"
    Space_Ambience = "Space Ambience"
    Space_Flyby = "Space Flyby"
    Space_Noise = "Space Noise"
    Splash = "Splash"
    Sport_Whistle_1 = "Sport Whistle 1"
    Sport_Whistle_2 = "Sport Whistle 2"
    Squeaky_Toy = "Squeaky Toy"
    Squish_Pop = "Squish Pop"
    Suction_Cup = "Suction Cup"
    Tada = "Tada"
    Telephone_Ring_2 = "Telephone Ring 2"
    Telephone_Ring = "Telephone Ring"
    Teleport_2 = "Teleport 2"
    Teleport_3 = "Teleport 3"
    Teleport = "Teleport"
    Tennis_Hit = "Tennis Hit"
    Thunder_Storm = "Thunder Storm"
    Toliet_Flush = "Toliet Flush"
    Toy_Honk = "Toy Honk"
    Toy_Zing = "Toy Zing"
    Traffic = "Traffic"
    Train_Breaks = "Train Breaks"
    Train_Horn_1 = "Train Horn 1"
    Train_Horn_2 = "Train Horn 2"
    Train_Horn_3 = "Train Horn 3"
    Train_On_Tracks = "Train On Tracks"
    Train_Signal_1 = "Train Signal 1"
    Train_Signal_2 = "Train Signal 2"
    Train_Start = "Train Start"
    Train_Whistle = "Train Whistle"
    Triumph = "Triumph"
    Tropical_Birds = "Tropical Birds"
    Wand = "Wand"
    Water_Drop = "Water Drop"
    Whistle_Thump = "Whistle Thump"
    Whiz_1 = "Whiz 1"
    Whiz_2 = "Whiz 2"
    Window_Breaks = "Window Breaks"
    Win = "Win"
    Wobble = "Wobble"
    Wood_Tap = "Wood Tap"
    Zip = "Zip"


class Image:
    """
    Available predefined images provided by the spike hub.
    """
    ANGRY = "ANGRY"
    ARROW_E = "ARROW_E"
    ARROW_N = "ARROW_N"
    ARROW_NE = "ARROW_NE"
    ARROW_NW = "ARROW_NW"
    ARROW_S = "ARROW_S"
    ARROW_SE = "ARROW_SE"
    ARROW_SW = "ARROW_SW"
    ARROW_W = "ARROW_W"
    ASLEEP = "ASLEEP"
    BUTTERFLY = "BUTTERFLY"
    CHESSBOARD = "CHESSBOARD"
    CLOCK1 = "CLOCK1"
    CLOCK10 = "CLOCK10"
    CLOCK11 = "CLOCK11"
    CLOCK12 = "CLOCK12"
    CLOCK2 = "CLOCK2"
    CLOCK3 = "CLOCK3"
    CLOCK4 = "CLOCK4"
    CLOCK5 = "CLOCK5"
    CLOCK6 = "CLOCK6"
    CLOCK7 = "CLOCK7"
    CLOCK8 = "CLOCK8"
    CLOCK9 = "CLOCK9"
    CONFUSED = "CONFUSED"
    COW = "COW"
    DIAMOND = "DIAMOND"
    DIAMOND_SMALL = "DIAMOND_SMALL"
    DUCK = "DUCK"
    FABULOUS = "FABULOUS"
    GHOST = "GHOST"
    GIRAFFE = "GIRAFFE"
    GO_RIGHT = "GO_RIGHT"
    GO_LEFT = "GO_LEFT"
    GO_UP = "GO_UP"
    GO_DOWN = "GO_DOWN"
    HAPPY = "HAPPY"
    HEART = "HEART"
    HEART_SMALL = "HEART_SMALL"
    HOUSE = "HOUSE"
    MEH = "MEH"
    MUSIC_CROTCHET = "MUSIC_CROTCHET"
    MUSIC_QUAVER = "MUSIC_QUAVER"
    MUSIC_QUAVERS = "MUSIC_QUAVERS"
    NO = "NO"
    PACMAN = "PACMAN"
    PITCHFORK = "PITCHFORK"
    RABBIT = "RABBIT"
    ROLLERSKATE = "ROLLERSKATE"
    SAD = "SAD"
    SILLY = "SILLY"
    SKULL = "SKULL"
    SMILE = "SMILE"
    SNAKE = "SNAKE"
    SQUARE = "SQUARE"
    SQUARE_SMALL = "SQUARE_SMALL"
    STICKFIGURE = "STICKFIGURE"
    SURPRISED = "SURPRISED"
    SWORD = "SWORD"
    TARGET = "TARGET"
    TORTOISE = "TORTOISE"
    TRIANGLE = "TRIANGLE"
    TRIANGLE_LEFT = "TRIANGLE_LEFT"
    TSHIRT = "TSHIRT"
    UMBRELLA = "UMBRELLA"
    XMAS = "XMAS"
    YES = "YES"


class Color:
    """
    Available colors
    """
    AZURE = "azure"
    BLACK = "black"
    BLUE = "blue"
    CYAN = "cyan"
    GREEN = "green"
    ORANGE = "orange"
    PINK = "pink"
    RED = "red"
    VIOLET = "violet"
    YELLOW = "yellow"
    WHITE = "white"

class Port:
    """
    Represents the ports on the spike hub.
    """
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'

class Gesture:
    """
    Gestures returned by gyroscope.
    """
    SHAKEN = "shaken"
    TAPPED = "tapped"
    DOUBLE_TAPPED = "double-tapped"
    FALLING = "falling"
    NONE = "none"


class StopAction:
    """
    The possible actions that will occur when stopping.
    """
    BRAKE = "brake"
    HOLD = "hold"
    COAST = "coast"


class Orientation:
    FRONT = "front"
    BACK = "back"
    UP = "up"
    DOWN = "down"
    LEFTSIDE = "leftside"
    RIGHTSIDE = "rightside"


class DistanceUnit:
    CM = "cm"
    INCH = "in"


class AdvancedDistanceUnit(DistanceUnit):
    PERCENT = "%"


class MotorUnit(AdvancedDistanceUnit):
    ROTATIONS = "rotations"
    DEGREES = "degrees"
    SECONDS = "seconds"


class App:
    """
    Represents the controller of the spike hub.
    """

    def play_sound(self, name: Sound, volume=100):
        """
        Plays a sound from the device (i.e., tablet or computer).
        The program will not continue until the sound has finished playing.

        Arguments:
            name: Name of the sound to play
            volume: Volume for the song to play (0-100%)
        Example:
            app = App()
            app.play_sound(Sound.Cat_Meow_1)
            """
        pass

    def start_sound(self, name: Sound, volume=100):
        """
        Starts playing a sound from your device (i.e., tablet or computer).
        The program will not wait for the sound to finish playing before proceeding to the next command.

        Arguments:
            name: Name of the sound to play
            volume: Volume for the song to play (0-100%)
        Example:
            app = App()
            app.start_sound(Sound.Cat_Meow_1)
            """
        pass


class Button:
    """
    Represents a button on the SpikeHub.
    """

    def wait_until_pressed(self):
        """
        Waits until the button is pressed.

        Example:
            hub = PrimeHub()
            # Beep every time the Left Button is pressed
            while True:
            hub.left_button.wait_until_pressed()
            hub.speaker.start_beep()
            hub.left_button.wait_until_released()
            hub.speaker.stop()
        """
        pass

    def wait_until_released(self):
        """
        Waits until the button is released.

        Example:
            hub = PrimeHub()
            ``# Beep every time the button is pressed
            while True:
            hub.left_button.wait_until_pressed()
            hub.speaker.start_beep()
            hub.left_button.wait_until_released()
            hub.speaker.stop()``
        """
        pass

    def was_pressed(self) -> bool:
        """
        Tests to see whether the button has been pressed since the last time this method called.
        Once this method returns "true," the button must be released and pressed again before it will return "true" again.

        Example:
             hub = PrimeHub()
             while True:
             wait_for_seconds(5)
             if hub.left_button.was_pressed():
             # Do something
        """
        pass

    def is_pressed(self) -> bool:
        """Tests whether the button is pressed.
        Returns:
            Weather the button is pressed
        """
        pass


class Component:
    def __init__(self, port: Port):
        """Defines a Component, this is an Object that has a port to it such as a Motor or a Color Sensor

        Parameters:
            port: Port of the component
        """
        self.port = port


class ColorSensor(Component):
    """
    Represents a Push-Button Sensor connected the spike hub.
    """
    def get_color(self) -> Color:
        """
        Retrieves the detected color of a surface.
        Returns:
        Name of Color
        """
        pass

    def get_ambient_light(self) -> int:
        """
        Retrieves the intensity of the ambient light.
        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in ambient light mode.
        Returns:
        The ambient light intensity. (0-100)
        """
        pass


    def get_reflected_light(self) -> int:
        """
        Retrieves the intensity of the reflected light.
        Returns:
        The reflected light intensity. (0-100)
        """
        pass


    def get_rgb_intensity(self) -> tuple:
        """
        Retrieves the overall color intensity, and intensity of red, green, and blue.
        Returns:
        Tumple of values [Red,Green,Blue] with a range of (0-1024)
        """
        pass


    def get_red(self) -> int:
        """
        Retrieves the color intensity of red.
        Returns:
        The color intensity of red. (0-1024)
        """
        pass


    def get_green(self) -> int:
        """
        Retrieves the color intensity of green.
        Returns:
        The color intensity of green. (0-1024)
        """
        pass


    def get_blue(self) -> int:
        """
        Retrieves the color intensity of blue.
        Returns:
        The color intensity of blue. (0-1024)
        """
        pass


    def wait_until_color(self, color: Color):
        """
        Waits until the Color Sensor detects the specified color.
        Parameters:
        color: The color to wait for.
        """
        pass


    def wait_for_new_color(self) -> Color:
        """
        Waits until the Color Sensor detects a new color.
        The first time this method is called, it immediately returns the detected color.
        After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.
        Returns:
        The new color.
        """
        pass


    def light_up_all(self, brightness=100) -> int:
        """
        Lights up all of the lights on the Color Sensor at the specified brightness.
        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in light up mode.
        Parameters:
        brightness: The desired brightness of the lights on the Color Sensor.
        """
        pass


    def light_up(self, light_1: int = 100, light_2: int = 100, light_3: int = 100):
        """
        Sets the brightness of the individual lights on the Color Sensor.
        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in light up mode.
        Parameters:
        light_1: The desired brightness of light 1.
        light_2: The desired brightness of light 2.
        light_3: The desired brightness of light 3.
        """
        pass



class DistanceSensor(Component):
    """
    Represents a Distance Sensor connected the spike hub.
    """
    def light_up_all(self, brightness: int = 100):
        """
        Lights up all of the lights on the Distance Sensor at the specified brightness.
        Parameters:
        brightness: The specified brightness of all of the lights.
        """
        pass

    def light_up(self, right_top: int = 100, left_top: int = 100, right_bottom: int = 100, left_bottom: int = 100):
        """
        Sets the brightness of the individual lights on the Distance Sensor.
        Parameters:
            right_top: The brightness of the light that’s above the right part of the Distance Sensor. (0-100)
            left_top: The brightness of the light that’s above the left part of the Distance Sensor. (0-100)
            right_bottom: The brightness of the light that’s below the right part of the Distance Sensor. (0-100)
            left_bottom: The brightness of the light that’s below the left part of the Distance Sensor. (0-100)
        """
        pass

    def get_distance_cm(self, short_range: bool = False) -> float:
        """
        Retrieves the measured distance in centimeters.
        Parameters:
            short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        Returns:
            The measured distance or "none" if the distance can't be measured. (0-200)cm
        """
        pass

    def get_distance_inches(self, short_range: bool = False) -> float:
        """
        Retrieves the measured distance in inches.
        Parameters:
            short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        Returns:
        The measured distance or "none" if the distance can't be measured. (0-79) inch
        """
        pass

    def get_distance_percentage(self, short_range: bool = False) -> int:
        """
        Retrieves the measured distance as a percentage.
        Parameters:
            short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        Returns:
            The measured distance or "none" if the distance can't be measured. (0-100)
        """
        pass

    def wait_for_distance_farther_than(self, distance: float, unit: AdvancedDistanceUnit = AdvancedDistanceUnit.CM, short_range: bool = False):
        """
        Waits until the measured distance is greater than the specified distance.
        Parameters:
            distance: The target distance to be detected from the sensor to an object.
            unit: The unit in which the distance is measured.
            short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        pass

    def wait_for_distance_closer_than(self, distance: float, unit: AdvancedDistanceUnit = AdvancedDistanceUnit.CM, short_range: bool = False):
        """
        Waits until the measured distance is less than the specified distance.
        Parameters:
            distance: The target distance to be detected from the sensor to an object.
            unit: The unit in which the distance is measured.
            short_range: Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
        """
        pass


class ForceSensor(Component):
    """
    Represents a Push-Button Sensor connected the spike hub.
    """
    def is_pressed(self) -> bool:
        """
        Tests whether the button on the sensor is pressed.
        Returns:
        True if the button is pressed.
        """
        pass

    def get_force_newton(self) -> float:
        """
        Retrieves the measured force, in newtons.
        Returns:
            The measured force, specified in newtons. (0-10)
        """
        pass

    def get_force_percentage(self) -> int:
        """
        Retrieves the measured force as a percentage of the maximum force.
        Returns:
            The measured force, given as a percentage. (0-100)
        """
        pass

    def wait_until_pressed(self):
        """
        Waits until the Force Sensor is pressed.
        """
        pass

    def wait_until_released(self):
        """
        Waits until the Force Sensor is released.
        """
        pass


class LightMatrix:
    """
    Represents the light matrix on the spike hub.
    """
    def show_image(self, image: Image, brightness: int = 100):
        """
        Shows an image on the Light Matrix.
        Parameters:
            image: Image to be displayed.
            brightness: Brightness of the image. (0-100)
        """
        pass

    def set_pixel(self, x: int, y: int, brightness: int = 100):
        """
        Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.
        Parameters:
            x: Pixel position, counting from the left. (1-5)
            y: Pixel position, counting from the top. (1-5)
            brightness: Brightness of the pixel (0-100)
        """
        pass

    def write(self, text: str):
        """
        Displays text on the Light Matrix, one letter at a time, scrolling from right to left.
        Your program will not continue until all of the letters have been shown.
        Parameters:
            text: Text to write.
        """
        pass

    def off(self):
        """
        Turns off all of the pixels on the Light Matrix.
        """
        pass


class MotionSensor:
    """
    Represents the gyroscope sensors in the spike hub.
    """
    def was_gesture(self, gesture: Gesture) -> bool:
        """
        Tests whether a gesture has occurred since the last time was_gesture() was used, or since the beginning of the program (for the first use).
        Parameters:
            gesture: The gesture to check
        """
        pass

    def wait_for_new_gesture(self) -> Gesture:
        """
        Waits until a new gesture happens.
        Returns:
            The new gesture.
        """
        pass

    def wait_for_new_orientation(self) -> Orientation:
        """
        Waits until the Hub’s orientation changes.
        The first time this method is called, it will immediately return the current value.
        After that, calling this method will block the program until the Hub’s orientation has changed since the previous time this method was called.
        Returns:
            The Hub’s new orientation.
        """
        pass

    def get_orientation(self) -> Orientation:
        """
        Retrieves the Hub's current orientation.
        Returns:
            The Hub’s current orientation.
        """
        pass

    def get_gesture(self) -> Gesture:
        """
        Retrieves the most recently-detected gesture.
        Returns:
            The gesture.
        """
        pass

    def get_roll_angle(self) -> int:
        """
        Retrieves the Hub’s roll angle.
        Roll is the rotation around the front-back (longitudinal) axis.
        Yaw is the rotation around the front-back (vertical) axis.
        Pitch is the rotation around the left-right (transverse) axis.
        Returns:
            The roll angle, specified in degrees. (-180:180)
        """
        pass

    def get_pitch_angle(self) -> int:
        """
        Retrieves the Hub’s pitch angle.
        Pitch is the rotation around the left-right (transverse) axis.
        Roll is the rotation around the front-back (longitudinal) axis.
        Yaw is the rotation around the front-back (vertical) axis.
        Returns:
            The pitch angle, specified in degrees. (-180:180)
        """
        pass

    def get_yaw_angle(self) -> int:
        """
        Retrieves the Hub’s yaw angle.
        Yaw is the rotation around the front-back (vertical) axis.
        Pitch is the rotation around the left-right (transverse) axis.
        Roll is the rotation around the front-back (longitudinal) axis.
        Returns:
            The yaw angle, specified in degrees. (-180:180)
        """
        pass

    def reset_yaw_angle(self):
        """
        Sets the yaw angle to 0.
        """
        pass


class Motor(Component):
    """
    Represents a Motor connected the spike hub.
    """
    def __init__(self, motor:Port):
        pass
    def run_to_position(self, degrees:int, direction: Direction=Direction.Shortest_path, speed: int=0):
        """
        Runs the motor to an absolute position.
        The sign of the speed will be ignored (i.e., absolute value), and the motor will always travel in the direction that’s been specified by the "direction" parameter.
        If the speed is greater than "100," it will be limited to "100."
        Parameters:
            degrees: The target position. (0:359)
            direction: The direction to use to reach the target position.
            speed: The motor’s speed.
        """
        pass
    def run_to_degrees_counted(self,degrees:int,speed:int=0):
        """
        Runs the motor until the number of degrees counted is equal to the value that has been specified by the "degrees" parameter.
        The sign of the speed will be ignored, and the motor will always travel in the direction required to reach the specified number of degrees.
        If the speed is greater than "100," it will be limited to "100."
        Parameters:
            degrees: The target degrees counted.
            speed: The desired speed. (0:100)
        """
        pass
    def run_for_degrees(self,degrees:int,speed:int=0):
        """
        Runs the motor for a specified number of degrees.
        Parameters:
            degrees: The number of degrees that the motor should run.
            speed: The motor’s speed. (-100:100)
        """
        pass
    def run_for_rotations(self,rotatins:int,speed:int=0):
        """
        Runs the motor for a specified number of rotations.
        Parameters:
        rotations: The number of rotations that the motor should run.
        speed: The motor’s speed. (-100:100)
        """
        pass
    def run_for_seconds(self,seconds:int,speed:int=0):
        """
        Runs the motor for a specified number of seconds.
        Parameters:
            seconds: The number of seconds for which the motor should run.
            speed: The motor’s speed. (-100:100)
        """
        pass
    def start(self,speed:int=0):
        """
        Starts running the motor at a specified speed.
        The motor will keep moving at this speed until you give it another motor command or when your program ends.
        Parameters:
            speed: The motor’s speed. (-100:100)
        """
        pass
    def stop(self):
        """
        Stops the motor.
        What the motor does after it stops depends on the action that’s been set in set_stop_action().
        The default value of set_stop_action() is "coast."
        """
        pass
    def start_at_power(self,power:int):
        """
        Starts rotating the motor at a specified power level.
        The motor will keep moving at this power level until you give it another motor command or when your program ends.
        Parameters:
            power: Power of the motor.
            speed: The motor’s speed. (-100:100)
        """
        pass
    def get_speed(self) -> int:
        """
        Retrieves the motor speed.
        Returns:
            The motor's current speed. (-100:100)
        """
        pass
    def get_position(self) -> int:
        """
        Retrieves the motor position.
        This is the clockwise angle between the moving marker and the zero-point marker on the motor.
        Returns:
            The motor’s position. (0:359)
        """
        pass
    def get_degrees_counted(self) -> int:
        """
        Retrieves the number of degrees that have been counted by the motor.
        Returns:
            The number of degrees that’s been counted.
        """
        pass
    def get_default_speed(self) -> int:
        """
        Retrieves the current default motor speed.
        Returns:
            The default motor’s speed. (-100:100)
        """
        pass
    def was_interrupted(self) -> bool:
        """
        Tests whether the motor was interrupted.
        Returns:
        True if the motor was interrupted since the last time was_interrupted() was called, otherwise false.
        """
        pass
    def was_stalled(self) -> bool:
        """
        Tests whether the motor was stalled.
        Returns:
        True if the motor has stalled since the last time was_stalled() was called, otherwise false.
        """
        pass
    def set_degrees_counted(self,degrees_counted:int):
        """
        Sets the "number of degrees counted" to the desired value.
        Parameters:
            degrees_counted: The value to which the number of degrees counted should be set.
        """
        pass
    def set_default_speed(self,default_speed:int):
        """
        Sets the default motor speed. This speed will be used when you omit the speed argument in one of the other methods, such as run_for_degrees.
        Setting the default speed does not affect any motors that are currently running.
        It will only have an effect when another motor method is called after this method.
        If the value of default_speed is outside of the allowed range, the default speed will be set to "-100" or "100" depending on whether the value is negative or positive.
        Parameters:
            default_speed: The default speed value. (-100:100)
        """
        pass
    def set_stop_action(self,action:StopAction):
        """
        Sets the default behavior when a motor stops.
        Parameters:
            action: The desired motor behavior when the motor stops.
        """
        pass
    def set_stall_detection(stop_when_stalled:bool):
        """
        Turns stall detection on or off.
        Stall detection senses when a motor has been blocked and can’t move.
        If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and the current motor command will be interrupted.
        If stall detection has been disabled, the motor will keep trying to run and programs will "get stuck" until the motor is no longer blocked.
        Stall detection is enabled by default.
        Parameters:
            stop_when_stalled: Choose true to enable stall detection or false to disable it.
        """
        pass

class MotorPair:
    """
    Represents a set of two motors connected to the spike hub
    """
    def __init__(self, motor_1: Port, motor_2: Port):
        pass

    def move(self, amount: float, unit: MotorUnit = MotorUnit.CM, steering: int = 0, speed: int = None):
        """
        Start both motors simultaneously to move a Driving Base.
        Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.
        The program will not continue until the specified value is reached.
        If the value of steering is equal to "-100" or "100," the Driving Base will perform a rotation on itself (i.e., "tank move") at the default speed of each motor.
        If the value of steering is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
        If speed is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
        If the speed is negative, the Driving Base will move backward instead of forward. Likewise, if the "amount" is negative, the Driving Base will move backward instead of forward. If both the speed and the "amount" are negative, the Driving Base will move forward.
        When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to the horizontal distance that the Driving Base will travel before stopping. The relationship between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().
        When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much the motor axle will turn before stopping.
        When the "unit" is "seconds," the "amount" parameter value specifies the duration that the motors will run before stopping.
        Parameters:
            amount: The quantity to move in relation to the specified unit of measurement.
            unit: The unit of measurement specified for the "amount" parameter.
            steering: The direction and quantity to steer the Driving Base. (-100:100)
            speed: The motor speed. (-100:100)
        """
        pass

    def start(self, steering: int = 0, speed: int = None):
        """
        Start both motors simultaneously to move a Driving Base.
        Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.
        The program flow is not interrupted. This is most likely interrupted by sensor input and a condition.
        If the value of steering is equal to "-100" or "100," the Driving Base will perform a rotation on itself (i.e., "tank move") at the default speed of each motor.
        If the value of "steering" is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
        If speed is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
        If the speed is negative, the Driving Base will move backward instead of forward. Likewise, if the "amount" is negative, the Driving Base will move backward instead of forward. If both the speed and the "amount" are negative, the Driving Base will move forward.
        Parameters:
            direction: The direction and quantity to steer the Driving Base. (-100:100)
            speed: The speed at which the Driving Base will move while performing a curve. (-100:100)
        """
        pass

    def stop(self):
        """
        Stops both motors simultaneously, which will stop a Driving Base.
        The motors will either actively hold their current position or coast freely depending on the option that’s been selected by set_stop_action().
        """
        pass

    def move_tank(self, amount: float, unit: MotorUnit = MotorUnit.CM, left_speed: int = None, right_speed: int = None):
        """
        Moves the Driving Base using differential (tank) steering.
        The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.
        When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to the horizontal distance that the Driving Base will travel before stopping. The relationship between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().
        When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much the motor axle will turn before stopping.
        When the "unit" is "seconds," the "amount" parameter value specifies the duration that the motors will run before stopping.
        If left_speed or right_speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
        If one of the speeds (i.e., left_speed or right_speed) is negative, the negative-speed motor will run backward instead of forward. If the "amount" parameter value is negative, both motors will rotate backward instead of forward. If both of the speed values (i.e., left_speed and right_speed) are negative and the "amount" parameter value is negative, both motors will rotate forward.
        The program will not continue until the specified value is reached.
        Parameters:
            amount: The quantity to move in relation to the specified unit of measurement.
            unit: The unit of measurement specified for the "amount" parameter.
            left_speed: The speed of the left motor. (-100:100)
            right_speed: The speed of the right motor. (-100:100)
        """
        pass

    def start_tank(self, left_speed: int, right_speed: int):
        """
        Starts moving the Driving Base using differential (tank) steering.
        The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.
        If left_speed or right_speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
        If the speed is negative, the motors will move backward instead of forward.
        The program flow is not interrupted. This is most likely interrupted by sensor input and a condition.
        Parameters:
            left_speed: The speed of the left motor. (-100:100)
            right_speed: The speed of the right motor. (-100:100)
        """
        pass

    def start_at_power(self, power: int, steering: int = 0):
        """
        Starts moving the Driving Base without speed control.
        The motors can also be driven without speed control. This is useful when using your own control algorithm (e.g., a proportional line-follower).
        If the steering is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
        If the power is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
        If the power is negative, the Driving Base will move backward instead of forward.
        The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.
        Parameters:
            power: The amount of power to send to the motors. (-100:100)
            steering: The steering direction (-100 to 100). "0" makes the Driving Base move straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right. (-100:100)
        """
        pass

    def start_tank_at_power(self,left_power:int,right_power:int):
        """
        Starts moving the Driving Base using differential (tank) steering without speed control.
        The motors can also be driven without speed control. This is useful when using your own control algorithm (e.g., a proportional line-follower).
        If the left_power or right_power is outside of the allowed range, the value will be rounded to "-100" or "100" depending on whether the value is positive or negative.
        If the power is a negative value, the corresponding motor will move backward instead of forward.
        The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.
        Parameters:
            left_power: The power of the left motor. (-100:100)
            right_power: The power of the right motor. (-100:100)
        """
        pass

    def get_default_speed(self) -> int:
        """
        Retrieves the default motor speed.
        Returns:
            The default motor speed. (-100:100)
        """
        pass

    def set_motor_rotation(self, amount: float = 17.6, unit: DistanceUnit = DistanceUnit.CM):
        """
        Sets the ratio of one motor rotation to the distance traveled.
        If there are no gears used between the motors and the wheels of the Driving Base, the "amount" is the circumference of one wheel.
        Calling this method does not affect the Driving Base if it’s already running. It will only have an effect the next time one of the move or start methods is used.
        Parameters:
            amount: The distance that the Driving Base moves when both motors move one rotation each.
            unit: The unit of measurement specified for the "amount" parameter.
        """
        pass

    def set_default_speed(self, speed: int = 100):
        """
        Sets the default motor speed.
        If speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
        Setting the speed will not have any effect until one of the move or start methods is called, even if the Driving Base is already moving.
        Parameters:
            speed: The default motor speed. (-100:100)
        """
        pass

    def set_stop_action(self, action: StopAction = StopAction.COAST):
        """
        Sets the motor action that will be used when the Driving Base stops.
        If the action is "brake," the motors will stop quickly and be allowed to turn freely.
        If the action is "hold," the motors will actively hold their current position and cannot be turned manually.
        If the action is set to "coast," the motors will stop slowly and can be turned freely.
        Setting the "stop" action does not take immediate effect on the motors. The setting will be saved and used whenever stop() is called or when one of the move methods has completed without being interrupted.
        Parameters:
            action: The desired action of the motors when the Driving Base stops.
        """
        pass


class Speaker:
    """
    Represents the speaker built in the spike hub.
    """
    def beep(self, note: float = 60, seconds: float = 0.2):
        """
        Plays a beep on the Hub.
        Your program will not continue until seconds have passed.
        Parameters:
            note: The MIDI note number. (44-123)
            seconds: The duration of the beep, specified in seconds.
        """
        pass
    def start_beep(self, note: float = 60):
        """
        Starts playing a beep.
        The beep will play indefinitely until stop() or another beep method is called.
        Parameters:
            note: The MIDI note number. (44-123)
        """
        pass

    def stop(self):
        """
        Stops any sound that is playing.
        """
        pass

    def get_volume(self) -> int:
        """
        Retrieves the value of the speaker volume.
        This only retrieves the volume of the Hub, not the programming app.
        Returns:
            The current volume. (0-100)
        """
        pass

    def set_volume(self, volume: int):
        """
        Sets the speaker volume.
        If the assigned volume is out of range, the nearest volume (i.e., 0 or 100) will be used instead.
        This only sets the volume of the Hub, not the programming app.
        Parameters:
            volume: The new volume percentage. (0-100)
        """
        pass


class StatusLight:
    """
    Represents the status light on the spike hub.
    """
    def on(self, color: Color = Color.WHITE):
        """
        Sets the color of the light.
        Parameters:
            color: Illuminates the Hub’s Brick Status Light in the specified color.
        """
        pass

    def off(self):
        """
        Turns off the light.
        """
        pass


class Timer:
    """
    An internal system to control use a timer.
    """
    def reset(self):
        """
        Sets the Timer to 0.
        """
        pass

    def now(self) -> int:
        """
        Retrieves the "right now" time of the Timer.
        Returns:
            The current time, specified in seconds.
        """
        pass

def wait_for_seconds(seconds: float):
    """
    Waits for a specified number of seconds before continuing the program.
    Parameters:
        seconds: The time to wait, specified in seconds.
    """
    pass



class PrimeHub:
    left_button = Button()
    right_button = Button()
    light_matrix = LightMatrix()
    motion_sensor = MotionSensor()
    speaker = Speaker()
    status_light = StatusLight()
