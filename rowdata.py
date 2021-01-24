import pygame, time, datetime, csv, pandas, math, numpy, pyrow

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (34, 54, 109)
light_blue = (25, 59, 255)
yellow = (255, 255, 0)
orange = (255, 115, 28)
red = (255, 0, 0)
dark_grey = (102, 102, 102)
light_grey = (40, 40, 40)
lighter_grey = (160, 160, 160)

# Setting up screen
pygame.init()
screen_width = (1000)
screen_height = (800)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Row Data")
clock = pygame.time.Clock()
FPS = 60

# Setting up fonts and font sizes
font = pygame.font.SysFont("C:\Windows\Fonts\Futura Md BT.ttf", 45)
smaller_font = 30
small_font = 45
medium_font = 60
large_font = 100

# importing logo image and getting dimensions of image
logo_img = pygame.image.load("RowData_logo.png")
logo_dimensions = logo_img.get_size()

# The variable 'user' will be used throughout the program
global user

# A function that is called every time the user presses a button
#def click():
    #pygame.mixer.music.load("click.mp3")
    #pygame.mixer.music.play(0, 0.0)

# Rendering text
def text_format(message, text_font, text_size, text_color):
    new_font = pygame.font.SysFont("C:\Windows\Fonts\Futura Md BT.ttf", text_size)
    new_text = new_font.render(message, 0, text_color)
    return new_text

# Code below written by someone else to draw the dashed line in the 'just_row' function
class Point:
    # constructed using a normal tuple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=1):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement/length

    for index in range(0, length/dash_length, 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)

# Log in and sign up screen
def log_in():
    # Initialise variables
    un_input_box = pygame.Rect(screen_width * 0.25, screen_height * 0.2, 140, 32)
    pw_input_box = pygame.Rect(screen_width * 0.25, screen_height * 0.3, 140, 32)
    log_button = pygame.Rect(screen_width * 0.2, screen_height * 0.4, 120, 50)
    sign_button = pygame.Rect(screen_width * 0.4, screen_height * 0.4, 120, 50)
    text_back = text_format("QUIT", font, small_font, white)
    back_rect = text_back.get_rect()
    back_button = pygame.Rect(back_rect.x + screen_width / 20, screen_height / 1.1, 120, 50)
    colour_inactive = pygame.Color('grey')
    colour_active = pygame.Color('white')
    un_colour = colour_active
    pw_colour = colour_inactive
    un_active = True
    pw_active = False
    global account_found
    account_found = True
    display_error = False
    un_input = ''
    pw_input = ''
    ast = ''
    done = False
    global user


    # function for when user attempts to log in
    def attempt_log_in(un_active, pw_active, un_input, pw_input):
        global account_found, user
        # Toggle the active variable to all false
        un_active = not un_active
        pw_active = not pw_active
        un_colour = colour_inactive
        pw_colour = colour_inactive
        # Open text file containing user's usernames and passwords
        user_file = open("user.txt", "r")
        # Split lines by comma and store in an array called accounts
        for line in user_file:
            accounts = line.split(",")
        # Compare each pair in the array accounts with user input
        for i in range(0, len(accounts), 2):
            if un_input == accounts[i] and pw_input == accounts[i+1]:
                user = un_input
                main_menu()
            else:
                account_found = False


    # Function for when user attempts to sign in
    def attempt_sign_up(un_input, pw_input):
        if un_input and pw_input != (""):
            global account_found, user
            user_file = open("user.txt", "a+")
            # Append user input to file split with commas
            user_file.write("," + un_input + "," + pw_input)
            user_file.close()
            user = un_input
            # Creates a workout csv file with their username in the name of the file ('user_username')
            with open('user_' + (str(un_input) + '.csv'), 'w') as user_workout_file:
                user_workout_file.close()
            main_menu()
        else:
            account_found = False


    # while loop for user interaction with log in screen
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # User interactions using the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the username input box
                if un_input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    un_active = not un_active
                    pw_active = False
                    un_colour = colour_active
                    pw_colour = colour_inactive
                # If the user clicked on the password input box
                elif pw_input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    pw_active = not pw_active
                    un_active = False
                    pw_colour = colour_active
                    un_colour = colour_inactive
                elif log_button.collidepoint(event.pos):
                    #click()
                    attempt_log_in(un_active, pw_active, un_input, pw_input)
                elif sign_button.collidepoint(event.pos):
                    #click()
                    attempt_sign_up(un_input, pw_input,)
                elif back_button.collidepoint(event.pos):
                    #click()
                    pygame.quit()
                # If the user clicks elsewhere on screen
                else:
                    # Toggle the active variable to all false
                    un_active = False
                    pw_active = False
                    un_colour = colour_inactive
                    pw_colour = colour_inactive

            # User interactions using the keyboard
            if event.type == pygame.KEYDOWN:
                if un_active or pw_active:
                    if event.key == pygame.K_TAB and un_active == True:
                        un_active = False
                        un_colour = colour_inactive
                        pw_active = True
                        pw_colour = colour_active
                    # If the user presses the return key
                    if event.key == pygame.K_RETURN:
                        attempt_log_in(un_active, pw_active, un_input, pw_input)
                    # If the user presses the return key and the username box is active
                    elif event.key == pygame.K_BACKSPACE and un_active == True:
                        un_input = un_input[:-1]
                    # If the user presses the return key and the password box is active
                    elif event.key == pygame.K_BACKSPACE and pw_active == True:
                        pw_input = pw_input[:-1]
                        ast = ast[:-1]
                    # If the user presses any other key
                    else:
                        if un_active:
                            un_input += event.unicode
                        elif pw_active and event.key != pygame.K_TAB:
                            pw_input += event.unicode
                            # Astrix outputted to screen for each password character inputted
                            ast += "*"

        # Fill background
        screen.fill(light_grey)

        # Wrong username and/or password
        if account_found == False:
                # Clears input boxes
                un_input = ''
                pw_input = ''
                ast = ''
                un_active = True
                un_colour = colour_active
                pw_active = False
                pw_colour = colour_inactive
                # Revert boolean variable to prevent the input boxes always resetting
                account_found = True
                display_error = True
        # Display error message if the account is not found
        if display_error == True:
            text_error = text_format("Incorrect Username and/or Password, please try again.", font, smaller_font, red)
            error_rect = text_error.get_rect()
            error_background = pygame.Rect(screen_width / 20, screen_height / 2, 550, 40)
            pygame.draw.rect(screen, white, error_background, 0)
            screen.blit(text_error, (error_background.x + (error_background[2] - error_rect[2]) / 2, error_background.y + (error_background[3] - error_rect[1]) / 4))


        # Drawing input box description, input box and log in/sign up buttons
        text_un = text_format("Username:", font, small_font, white)
        text_pw = text_format("Password:", font, small_font, white)
        text_log = text_format("Log in", font, small_font, white)
        text_sign = text_format("Sign up", font, small_font, white)
        un_rect = text_un.get_rect()
        pw_rect = text_pw.get_rect()
        log_rect = text_log.get_rect()
        sign_rect = text_sign.get_rect()
        pygame.draw.rect(screen, un_colour, un_input_box, 0)
        pygame.draw.rect(screen, pw_colour, pw_input_box, 0)
        pygame.draw.rect(screen, blue, log_button, 0)
        pygame.draw.rect(screen, blue, sign_button, 0)
        pygame.draw.rect(screen, blue, back_button, 0)
        screen.blit(logo_img, (screen_width / 2 - (logo_dimensions[0] / 2), screen_height * 1 / 40))
        screen.blit(text_un, (un_input_box.x - un_rect[2], un_input_box.y))
        screen.blit(text_pw, (pw_input_box.x - pw_rect[2], pw_input_box.y))
        screen.blit(text_log, (log_button.x + (log_button[2] - log_rect[2]) / 2, log_button.y + (log_button[3] - log_rect[1]) / 4))
        screen.blit(text_sign, (sign_button.x + (sign_button[2] - sign_rect[2]) / 2, sign_button.y + (sign_button[3] - sign_rect[1]) / 4))
        screen.blit(text_back, (back_button.x + (back_button[2] - back_rect[2]) / 2, back_button.y + (back_button[3] - back_rect[1]) / 4))
        # Render the text
        un_txt_surface = font.render(un_input, True, black)
        pw_txt_surface = font.render(ast, True, black)
        # Resize the box if the text is too long
        un_width = max(200, un_txt_surface.get_width() + 10)
        un_input_box.w = un_width
        pw_width = max(200, pw_txt_surface.get_width() + 10)
        pw_input_box.w = pw_width
        # Blit the text
        screen.blit(un_txt_surface, (un_input_box.x, un_input_box.y))
        screen.blit(pw_txt_surface, (pw_input_box.x, pw_input_box.y))
        pygame.display.flip()
        clock.tick(60)


# Main menu
def main_menu():

    # Initialise variables
    main_menu = True
    selected = ""
    rect_dimensions = (450, 300)

    text_just_row = text_format("JUST ROW", font, medium_font, black)
    text_custom = text_format("CUSTOM ROW", font, medium_font, black)
    text_stats = text_format("STATISTICS", font, medium_font, black)
    text_sign_out = text_format("SIGN OUT", font, medium_font, black)
    text_quit = text_format("QUIT", font, medium_font, black)

    just_row_rect = text_just_row.get_rect()
    custom_rect = text_custom.get_rect()
    stats_rect = text_stats.get_rect()
    sign_out_rect = text_sign_out.get_rect()
    quit_rect = text_quit.get_rect()

    while main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Text = white when selected, Text = black when not selected
            if selected == "just_row":
                text_just_row = text_format("JUST ROW", font, medium_font, white)
            else:
                text_just_row = text_format("JUST ROW", font, medium_font, black)
            if selected == "custom":
                text_custom = text_format("CUSTOM ROW", font, medium_font, white)
            else:
                text_custom = text_format("CUSTOM ROW", font, medium_font, black)
            if selected == "stats":
                text_stats = text_format("STATISTICS", font, medium_font, white)
            else:
                text_stats = text_format("STATISTICS", font, medium_font, black)
            if selected == "sign_out":
                text_sign_out = text_format("SIGN OUT", font, medium_font, white)
            else:
                text_sign_out = text_format("SIGN OUT", font, medium_font, black)
            if selected == "quit":
                text_quit = text_format("QUIT", font, medium_font, white)
            else:
                text_quit = text_format("QUIT", font, medium_font, black)

            # If the mouse position is over a text option, turn the text to white
            mouse = pygame.mouse.get_pos()
            if (screen_width / 2 - (just_row_rect[2] / 2)) + just_row_rect[2] > mouse[0] > (screen_width / 2 - (just_row_rect[2] / 2)) and (screen_height / 2 - (rect_dimensions[1] / 2) + 2 * just_row_rect[3]) > mouse[1] > (screen_height / 2 - (rect_dimensions[1] / 2) + just_row_rect[3]):
                selected = "just_row"
            elif (screen_width / 2 - (custom_rect[2] / 2)) + custom_rect[2] > mouse[0] > (screen_width / 2 - (custom_rect[2] / 2)) and (screen_height / 2 - (rect_dimensions[1] / 2) + 3 * custom_rect[3]) > mouse[1] > (screen_height / 2 - (rect_dimensions[1] / 2) + 2 * custom_rect[3]):
                selected = "custom"
            elif (screen_width / 2 - (stats_rect[2] / 2)) + stats_rect[2] > mouse[0] > (screen_width / 2 - (stats_rect[2] / 2)) and (screen_height / 2 - (rect_dimensions[1] / 2) + 4 * stats_rect[3]) > mouse[1] > (screen_height / 2 - (rect_dimensions[1] / 2) + 3 * stats_rect[3]):
                selected = "stats"
            elif (screen_width / 2 - (sign_out_rect[2] / 2)) + sign_out_rect[2] > mouse[0] > (screen_width / 2 - (sign_out_rect[2] / 2)) and (screen_height / 2 - (rect_dimensions[1] / 2) + 5 * sign_out_rect[3]) > mouse[1] > (screen_height / 2 - (rect_dimensions[1] / 2) + 4 * sign_out_rect[3]):
                selected = "sign_out"
            elif (screen_width / 2 - (quit_rect[2] / 2)) + quit_rect[2] > mouse[0] > (screen_width / 2 - (quit_rect[2] / 2)) and (screen_height / 2 - (rect_dimensions[1] / 2) + 6 * quit_rect[3]) > mouse[1] > (screen_height / 2 - (rect_dimensions[1] / 2) + 5 * quit_rect[3]):
                selected = "quit"
            else:
                selected = ""

            # Determines what happens when an option is selected when pressing enter
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected == "just_row":
                    #click()
                    just_row(False, False, 0, 0)
                if selected == "custom":
                    #click()
                    custom()
                if selected == "stats":
                    #click()
                    stats()
                if selected == "sign_out":
                    #click()
                    log_in()
                if selected == "quit":
                    #click()
                    pygame.quit()
                    quit()

        # Fill background and render text
        screen.fill(light_grey)
        pygame.draw.rect(screen, dark_grey, [screen_width / 2 - (rect_dimensions[0] / 2), screen_height / 2 - (rect_dimensions[1] / 2), rect_dimensions[0], rect_dimensions[1]])
        screen.blit(logo_img, (screen_width / 2 - (logo_dimensions[0]/2), 60))
        screen.blit(text_just_row, (screen_width / 2 - (just_row_rect[2] / 2), (screen_height / 2 - (rect_dimensions[1] / 2) + just_row_rect[3])))
        screen.blit(text_custom, (screen_width / 2 - (custom_rect[2] / 2), (screen_height / 2 - (rect_dimensions[1] / 2) + 2 * custom_rect[3])))
        screen.blit(text_stats, (screen_width / 2 - (stats_rect[2] /2), (screen_height / 2 - (rect_dimensions[1] / 2) + 3 * stats_rect[3])))
        screen.blit(text_sign_out, (screen_width / 2 - (sign_out_rect[2] / 2), (screen_height / 2 - (rect_dimensions[1] / 2) + 4 * sign_out_rect[3])))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), (screen_height / 2 - (rect_dimensions[1] / 2) + 5 * quit_rect[3])))

        pygame.display.update()
        clock.tick(FPS)

# Just Row (No workout set)
def just_row(time_workout, distance_workout, ti_input, di_input):

    # Initialise Variables
    rowing = True
    save_required = False

    one_third_x = (333.0 / screen_width) * screen_width
    two_third_x = (666.0 / screen_width) * screen_width
    first_line = (150.0 / screen_height) * screen_height
    second_line = (350.0 / screen_height) * screen_height
    third_line = (500.0 / screen_height) * screen_height

    water = pygame.Rect(0, third_line + 3.5, screen_width, 220)

    boat_pb = pygame.image.load("boat_pb.png")
    boat_pb_scaled = pygame.transform.scale(boat_pb, (150, 45))
    boat_pb_dimensions = boat_pb_scaled.get_size()
    boat_pb_x = 0

    boat_1 = pygame.image.load("boat_1.png")
    boat_1_scaled = pygame.transform.scale(boat_1, (150, 45))
    boat_1_dimensions = boat_1_scaled.get_size()
    boat_1_x = 0

    green_boat_1 = pygame.image.load("green_boat_1.png")
    green_boat_1_scaled = pygame.transform.scale(green_boat_1, (150, 45))
    green_boat_1_dimensions = green_boat_1_scaled.get_size()

    red_boat_1 = pygame.image.load("red_boat_1.png")
    red_boat_1_scaled = pygame.transform.scale(red_boat_1, (150, 45))
    red_boat_1_dimensions = red_boat_1_scaled.get_size()

    store_pace = []
    store_cadence = []
    store_calories = []
    store_power = []
    store_heartrate = []

    screen.fill(blue)

    pace_input = 0
    duration_input = 0
    distance_input = 0
    cadence_input = 0
    calories_input = 0
    power_input = 0
    heartrate_input = 0

    progress = 0

    first_distance_workout = False
    first_time_workout = False

    global user

    # Continues through the while loop until a rowing machine is connected, this enables the user to connect the rowing machine while the program is running.
    ergs = list(pyrow.find())
    while len(ergs) == 0:
        ergs = list(pyrow.find())
    erg = pyrow.pyrow(ergs[0])
    print("Connected to Rowing Machine")

    workout = erg.get_workout()
    print("Waiting for workout to start")
    while workout['state'] == 0:
        time.sleep(1)
        workout = erg.get_workout()
    print("Workout has begun")

    # If the user has chosen a distance custom workout from the custom workout screen
    if distance_workout == True:
        # Opens and reads the user's workout file using Panda
        csv_file = r'user_' + (str(user) + '.csv')
        df = pandas.read_csv(csv_file, names=['avg_pace_seconds', 'duration_seconds', 'distance_input', 'avg_cadence', 'avg_calories', 'avg_power', 'avg_heartrate'])
        # Arrays of all distances and durations logged in the file
        distances = df.distance_input
        durations = df.duration_seconds
        no_of_rows = len(df)
        durations_of_specific_distance = []
        # Searches through the rows to find distances that match the distance entered by the user in 'custom_workout'
        for i in range(0, no_of_rows):
            if str(distances[i]) == di_input:
                # Appends all durations of each workout that is equal to the distance entered by the user in 'custom_workout'
                durations_of_specific_distance.append(durations[i])
        # If the user has completed that workout before, their personal best will be the min value in the array of durations
        if durations_of_specific_distance != []:
            custom_time = min(durations_of_specific_distance)
        # If the user has not completed the workout before, set a boolean to 'True' to show that this is the case
        else:
            first_distance_workout = True
            first_time_workout = False

    # If the user has chosen a timed custom workout from the custom workout screen
    if time_workout == True:
        csv_file = r'user_' + (str(user) + '.csv')
        df = pandas.read_csv(csv_file, names=['avg_pace_seconds', 'duration_seconds', 'distance_input', 'avg_cadence', 'avg_calories', 'avg_power', 'avg_heartrate'])
        # Arrays of all distances and durations logged in the file
        durations = df.duration_seconds
        distances = df.distance_input
        no_of_rows = len(df)
        distances_of_specific_times = []
        # Searches through the rows to find durations that match the durations entered by the user in 'custom_workout'
        for i in range(0, no_of_rows):
            if str(durations[i]) == str(ti_input):
                # Appends all distances of each workout that is equal to the duration entered by the user in 'custom_workout'
                distances_of_specific_times.append(distances[i])
        # If the user has completed that workout before, their personal best will be the min value in the array of distances
        if distances_of_specific_times != []:
            custom_distance = min(distances_of_specific_times)
        # If the user has not completed the workout before, set a boolean to 'True' to show that this is the case
        else:
            first_time_workout = True
            first_distance_workout = False

    # While the user is rowing
    while rowing: #and workout['state'] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicks the 'Save & Quit' button, set the save 'save_required' boolean to True
                if save_button.collidepoint(event.pos):
                    #click()
                    save_required = True
                # If the user clicks the 'Rest' button, restart the 'just_row' function
                elif reset_button.collidepoint(event.pos):
                    #click()
                    just_row(time_workout, distance_workout,  ti_input, di_input)


        # Get data from rowing machine using CSAFE commands and formats each with units
        pace_input = erg.send(['CSAFE_GETPACE_CMD', ])
        pace_seconds = (pace_input['CSAFE_GETPACE_CMD'][0] / 2)
        pace_formatted = (str(datetime.timedelta(seconds = (pace_input['CSAFE_GETPACE_CMD'][0] / 2))))[3:7]

        duration_input = erg.send(['CSAFE_PM_GET_WORKTIME', ])
        duration_seconds = (duration_input['CSAFE_PM_GET_WORKTIME'][0] / 100)
        duration_formatted = str(datetime.timedelta(seconds = (duration_input['CSAFE_PM_GET_WORKTIME'][0] / 100)))

        distance_input = erg.send(['CSAFE_GETHORIZONTAL_CMD', ])
        distance_formatted = str(distance_input['CSAFE_GETHORIZONTAL_CMD'][0]) + "m"

        cadence_input = erg.send(['CSAFE_GETCADENCE_CMD', ])
        cadence_formatted = str(cadence_input['CSAFE_GETCADENCE_CMD'][0]) + " SPM"

        calories_input = erg.send(['CSAFE_GETCALORIES_CMD', ])
        calories_formatted = str(calories_input['CSAFE_GETCALORIES_CMD'][0]) + " Cal"

        power_input = erg.send(['CSAFE_GETPOWER_CMD', ])
        power_formatted = str(power_input['CSAFE_GETPOWER_CMD'][0]) + "W"

        heartrate_input = erg.send(['CSAFE_GETHRCUR_CMD', ])
        heartrate_formatted = str(heartrate_input['CSAFE_GETHRCUR_CMD'][0]) + " BPM"

        """
        pace_input += 0.1
        pace_seconds = pace_input / 2
        pace_formatted = (str(datetime.timedelta(seconds = (int(pace_seconds)))))[3:7]
        duration_input += 1
        duration_seconds = duration_input
        duration_formatted = str(datetime.timedelta(seconds = (int(duration_input))))
        distance_input += 1
        distance_formatted = str(int(distance_input)) + "m"
        cadence_input += 0.1
        cadence_formatted = str(int(cadence_input)) + " S/M"
        calories_input += 0.1
        calories_formatted = str(int(calories_input)) + " Cal"
        power_input += 0.1
        power_formatted = str(int(power_input)) + "W"
        heartrate_input += 0.1
        heartrate_formatted = str(int(heartrate_input)) + " B/M"
        """

        # Averages each peice of data from the rowing machine each time through the while loop
        def average(array, data_input):
            array.append(data_input)
            data_average = sum(array) / len(array)
            return data_average

        avg_pace_seconds = average(store_pace, pace_seconds)
        avg_cadence = average(store_cadence, cadence_input)
        avg_calories = average(store_calories, calories_input)
        avg_power = average(store_power, power_input)
        avg_heartrate = average(store_heartrate, heartrate_input)

        # An array of all averages of each piece of data from the rowing machine
        workout_data = (int(avg_pace_seconds), int(duration_seconds), int(distance_input), int(avg_cadence), int(avg_calories), int(avg_power), int(avg_heartrate))

        # If the user is doing a custom distance workout, their progress as a percentage is calculated
        if distance_workout == True:
            # Calculates Percentage and distance left of a custom distance workout
            # Only displaying appropriate number of digits depending on each value
            if (float(distance_input) / float(di_input)) * 100 < 10:
                progress = str((float(distance_input) / float(di_input)) * 100)[0] + '%'
            else:
                progress = str((float(distance_input) / float(di_input)) * 100)[0:2] + '%'
            if float(di_input) - float(distance_input) < 1000:
                left = 'Distance remaining: ' + str(float(di_input) - float(distance_input))[0:3] + 'm'
            elif float(di_input) - float(distance_input) > 9999:
                left = 'Distance remaining: ' + str(float(di_input) - float(distance_input))[0:5] + 'm'
            else:
                left = 'Distance remaining: ' + str(float(di_input) - float(distance_input))[0:4] + 'm'
        # If the user is doing a custom timed workout, their progress as a percentage is calculated
        if time_workout == True:
            # Calculates Percentage and time left of a custom distance workout
            # Only displaying appropriate number of digits depending on each value
            if (float(duration_input) / float(ti_input)) * 100 < 10:
                progress = str((float(duration_input) / float(ti_input)) * 100)[0] + '%'
            else:
                progress = str((float(duration_input) / float(ti_input)) * 100)[0:2] + '%'
            left = 'Time remaining: ' + str(datetime.timedelta(seconds=((float(ti_input) - float(duration_input)) / 60)))[3:10]

        if time_workout == True or distance_workout == True:
            # Formatting progress to be displayed on screen
            progress_text = text_format(progress, font, 60, white)
            left_text = text_format(left, font, 50, white)


        # Fill Background and lines that divides each data item
        screen.fill(blue)
        pygame.draw.line(screen, lighter_grey, (0, first_line), (screen_width, first_line), 2)
        pygame.draw.line(screen, lighter_grey, (0, second_line), (screen_width, second_line), 2)
        pygame.draw.line(screen, lighter_grey, (0, third_line), (screen_width, third_line), 4)
        pygame.draw.line(screen, lighter_grey, (one_third_x, 0), (one_third_x, first_line), 2)
        pygame.draw.line(screen, lighter_grey, (two_third_x, 0), (two_third_x, first_line), 2)
        pygame.draw.line(screen, lighter_grey, (one_third_x, second_line), (one_third_x, third_line), 2)
        pygame.draw.line(screen, lighter_grey, (two_third_x, second_line), (two_third_x, third_line), 2)
        pygame.draw.rect(screen, light_blue, water, 0)
        #draw_dashed_line(screen, orange, (0, third_line + screen_height / 7.1), (screen_width, third_line + screen_height / 7.1), width = 8, dash_length = 8)

        # If user is doing a distance custom workout and has done it before
        if distance_workout == True and first_distance_workout == False:
            # Set the x coordinate of each boat
            boat_pb_x = duration_seconds / (float(custom_time) / screen_width)
            boat_1_x = distance_input / (float(di_input) / screen_width)
            #if distance_input / 2 == di_input:
                #click()
        # If this is the first time the user has done this custom workout
        elif first_distance_workout == True:
            # Set the x coordinate of the user's boat only as there is no personal best for that custom workout
            boat_1_x = distance_input / (float(di_input) / screen_width)

        # If user is doing a timed custom workout and has done it before
        if time_workout == True and first_time_workout == False:
            # Set the x coordinate of each boat
            boat_pb_x = duration_seconds / (float(custom_distance) / screen_width)
            boat_1_x = distance_input / (float(ti_input) / screen_width)
        # If this is the first time the user has done this custom workout
        elif first_time_workout == True:
            # Set the x coordinate of the user's boat only as there is no personal best for that custom workout
            boat_1_x = distance_input / (float(ti_input) / screen_width)

        # Render the boats and data from the rowing machine
        # If the user is ahead of their personal best, their boat will be green. If it's behind, it will be red
        if first_time_workout == False and first_distance_workout == False:
            if boat_pb_x < boat_1_x:
                screen.blit(boat_pb_scaled, (boat_pb_x - boat_pb_dimensions[0], third_line + boat_pb_dimensions[1] / 2 + 12))
                screen.blit(green_boat_1_scaled, (boat_1_x - boat_1_dimensions[0], third_line + screen_height / 7 + boat_1_dimensions[1] / 2 + 11))
            elif boat_pb_x > boat_1_x:
                screen.blit(boat_pb_scaled, (boat_pb_x - boat_pb_dimensions[0], third_line + boat_pb_dimensions[1] / 2 + 12))
                screen.blit(red_boat_1_scaled, (boat_1_x - boat_1_dimensions[0], third_line + screen_height / 7 + boat_1_dimensions[1] / 2 + 11))
            else:
                screen.blit(boat_pb_scaled, (boat_pb_x - boat_pb_dimensions[0], third_line + boat_pb_dimensions[1] / 2 + 12))
                screen.blit(boat_1_scaled, (boat_1_x - boat_1_dimensions[0], third_line + screen_height / 7 + boat_1_dimensions[1] / 2 + 11))
        else:
            screen.blit(boat_pb_scaled, (boat_pb_x - boat_pb_dimensions[0], third_line + boat_pb_dimensions[1] / 2 + 12))
            screen.blit(boat_1_scaled, (boat_1_x - boat_1_dimensions[0], third_line + screen_height / 7 + boat_1_dimensions[1] / 2 + 11))

        if time_workout == True or distance_workout == True:
            screen.blit(progress_text, (screen_width * 0.02, screen_height * 0.93))
            screen.blit(left_text, (screen_width * 0.12, screen_height * 0.933))

        pace_text = text_format(pace_formatted, font, 300, white)
        pace_rect = pace_text.get_rect()
        screen.blit(pace_text, ((screen_width / 2) - (pace_rect[2] / 2), ((second_line - first_line) / 2 + first_line - pace_rect[3] / 2 + 10)))

        duration_text = text_format(duration_formatted, font, 130, white)
        duration_rect = duration_text.get_rect()
        screen.blit(duration_text, (screen_width * (1.0 / 6.0) - (duration_rect[2] / 2), (first_line / 2 - duration_rect[3] / 2)))

        distance_text = text_format(distance_formatted, font, 120, white)
        distance_rect = distance_text.get_rect()
        screen.blit(distance_text, (screen_width / 2 - (distance_rect[2] / 2), (first_line / 2 - distance_rect[3] / 2)))
        
        cadence_text = text_format(cadence_formatted, font, 130, white)
        cadence_rect = cadence_text.get_rect()
        screen.blit(cadence_text, (screen_width * (5.0 / 6.0) - (cadence_rect[2] / 2), (first_line / 2 - cadence_rect[3] / 2)))

        calories_text = text_format(calories_formatted, font, 130, white)
        calories_rect = calories_text.get_rect()
        screen.blit(calories_text, (screen_width * (1.0 / 6.0) - (calories_rect[2] / 2), ((third_line - second_line) / 2 + second_line - calories_rect[3] / 2)))

        power_text = text_format(power_formatted, font, 130, white)
        power_rect = power_text.get_rect()
        screen.blit(power_text, (screen_width / 2 - (power_rect[2] / 2), ((third_line - second_line) / 2 + second_line - power_rect[3] / 2)))

        heartrate_text = text_format(heartrate_formatted, font, 130, white)
        heartrate_rect = heartrate_text.get_rect()
        screen.blit(heartrate_text, (screen_width * (5.0 / 6.0) - (heartrate_rect[2] / 2), ((third_line - second_line) / 2 + second_line - heartrate_rect[3] / 2)))

        # Render 'Save & Quit' and 'Reset' buttons
        save_button = pygame.Rect(screen_width * 0.65, screen_height * 0.92, 200, 50)
        reset_button = pygame.Rect(screen_width * 0.87, screen_height * 0.92, 110, 50)
        save_text = text_format("Save & Exit", font, small_font, white)
        reset_text = text_format("Reset", font, small_font, white)
        save_rect = save_text.get_rect()
        reset_rect = reset_text.get_rect()
        pygame.draw.rect(screen, black, save_button, 0)
        pygame.draw.rect(screen, black, reset_button, 0)
        screen.blit(save_text, (save_button.x + (save_button[2] - save_rect[2]) / 2, save_button.y + ((save_button[3] - save_rect[3]) / 2)))
        screen.blit(reset_text, (reset_button.x + (reset_button[2] - reset_rect[2]) / 2, reset_button.y + ((reset_button[3] - reset_rect[3]) / 2)))

        # If the user is doing a custom workout
        if distance_workout or time_workout == True:
            # If the user has reached the end of their custom workout
            if (int(distance_input) == int(di_input)) and distance_workout == True or (int(duration_input) == int(ti_input)) and time_workout == True:
                save_required = True

        if save_required:
            # Opens user's workout file and appends their workout_data to a new line
            with open('user_' + (str(user) + '.csv'), 'a+') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(workout_data)
                csv_file.close()
            summary(pace_formatted, duration_formatted, workout_data)

        pygame.display.flip()
        clock.tick(FPS)

# A summary of the workout is displayed to the user after their workout
def summary(pace_formatted, duration_formatted, workout_data):

    viewing = True
    global user

    while viewing == True:

        # Fill Background and render formatted workout data
        screen.fill(light_grey)

        title = text_format(user + "'s SUMMARY", font, large_font, white)
        title_rect = title.get_rect()
        screen.blit(title, (screen_width / 2 - title_rect[2] / 2, screen_height / 20))

        text_avg_user_pace = text_format("Average Pace:  " + str(pace_formatted), font, small_font, white)
        avg_user_pace_rect = text_avg_user_pace.get_rect()
        screen.blit(text_avg_user_pace, (avg_user_pace_rect.x + screen_width / 20, screen_height / 6))

        text_avg_user_duration = text_format("Time Rowed:  " + str(duration_formatted), font, small_font, white)
        avg_user_duration_rect = text_avg_user_duration.get_rect()
        screen.blit(text_avg_user_duration, (avg_user_duration_rect.x + screen_width / 20, screen_height / 6 + avg_user_duration_rect[3] * 2))

        text_avg_user_distance = text_format("Distance Rowed:  " + str(workout_data[2]) + "m", font, small_font, white)
        avg_user_distance_rect = text_avg_user_distance.get_rect()
        screen.blit(text_avg_user_distance, (avg_user_distance_rect.x + screen_width / 20, screen_height / 6 + avg_user_distance_rect[3] * 4))

        text_avg_user_cadence = text_format("Average cadence:  " + str(workout_data[3]) + " S/M", font, small_font, white)
        avg_user_cadence_rect = text_avg_user_cadence.get_rect()
        screen.blit(text_avg_user_cadence, (avg_user_cadence_rect.x + screen_width / 20, screen_height / 6 + avg_user_cadence_rect[3] * 6))

        text_avg_user_calories = text_format("Calories Burnt:  " + str(workout_data[4]), font, small_font, white)
        avg_user_calories_rect = text_avg_user_calories.get_rect()
        screen.blit(text_avg_user_calories, (avg_user_calories_rect.x + screen_width / 20, screen_height / 6 + avg_user_calories_rect[3] * 8))

        text_avg_user_power = text_format("Average Power:  " + str(workout_data[5]) + "W", font, small_font, white)
        avg_user_power_rect = text_avg_user_power.get_rect()
        screen.blit(text_avg_user_power, (avg_user_power_rect.x + screen_width / 20, screen_height / 6 + avg_user_power_rect[3] * 10))

        text_avg_user_heartrate = text_format("Heart Rate:  " + str(workout_data[6]) + " B/M", font, small_font, white)
        avg_user_heartrate_rect = text_avg_user_heartrate.get_rect()
        screen.blit(text_avg_user_heartrate, (avg_user_heartrate_rect.x + screen_width / 20, screen_height / 6 + avg_user_heartrate_rect[3] * 12))

        # Render 'Back" button to take the user to the main menu
        text_back = text_format("BACK", font, small_font, white)
        back_rect = text_back.get_rect()
        back_button = pygame.Rect(back_rect.x + screen_width / 20, screen_height / 1.1, 120, 50)
        pygame.draw.rect(screen, blue, back_button, 0)
        screen.blit(text_back, (back_button.x + (back_button[2] - back_rect[2]) / 2, back_button.y + (back_button[3] - back_rect[1]) / 4))

        # Handles mouse clicks from the user
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                #click()
                viewing = False
            if event.type == pygame.K_SPACE:
                viewing = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if viewing == False:
            main_menu()

        pygame.display.update()
        clock.tick(FPS)

# User enters a distance or time in this screen to complete a custom workout and race against their personal best
def custom():

    # Initialise Variables
    time_input_box = pygame.Rect(screen_width * 0.56, screen_height * 0.25, 70, 32)
    distance_input_box = pygame.Rect(screen_width * 0.56, screen_height * 0.35, 70, 32)
    time_button = pygame.Rect(screen_width * 0.28, screen_height * 0.45, 180, 50)
    distance_button = pygame.Rect(screen_width * 0.48, screen_height * 0.45, 220, 50)
    colour_inactive = pygame.Color('grey')
    colour_active = pygame.Color('white')
    ti_colour = colour_active
    di_colour = colour_inactive
    ti_active = True
    di_active = False
    ti_input = ''
    di_input = ''
    value = ''
    done = False
    int_error = False
    ti_len_error = False
    di_len_error = False
    display_error = False

    # while loop for user interaction with log in screen
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # User interactions using the mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the username input box
                if time_input_box.collidepoint(event.pos):
                    #click()
                    # Toggle the active variable.
                    ti_active = not ti_active
                    di_active = False
                    ti_colour = colour_active
                    di_colour = colour_inactive
                # If the user clicked on the password input box
                elif distance_input_box.collidepoint(event.pos):
                    #click()
                    # Toggle the active variable.
                    di_active = not di_active
                    ti_active = False
                    di_colour = colour_active
                    ti_colour = colour_inactive
                elif time_button.collidepoint(event.pos):
                    #click()
                    # Validation for timed inputs
                    try:
                        # Checks that the input is an integer
                        value = int(ti_input)
                    except ValueError:
                        int_error = True
                    # Checks that the input is within range
                    if 1 <= value <= 599:
                        ti_input = int(ti_input) * 60
                        just_row(True, False, ti_input, 0)
                    else:
                        ti_len_error = True
                elif distance_button.collidepoint(event.pos):
                    #click()
                    try:
                        # Checks that the input is an integer
                        value = int(di_input)
                    except ValueError:
                        int_error = True
                    # Checks that the input is within range
                    if 200 <= value <= 20000:
                        just_row(False, True, 0, di_input)
                    else:
                        di_len_error = True
                elif event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                    #click()
                    main_menu()
                # If the user clicks elsewhere on screen
                else:
                    # Toggle the active variable to all false
                    ti_active = False
                    di_active = False
                    ti_colour = colour_inactive
                    di_colour = colour_inactive

            # User interactions using the keyboard
            if event.type == pygame.KEYDOWN:
                if ti_active or di_active:
                    if event.key == pygame.K_TAB and ti_active == True:
                        ti_active = False
                        ti_colour = colour_inactive
                        di_active = True
                        di_colour = colour_active
                    # If the user presses the return key and the username box is active
                    elif event.key == pygame.K_BACKSPACE and ti_active == True:
                        ti_input = ti_input[:-1]
                    # If the user presses the return key and the password box is active
                    elif event.key == pygame.K_BACKSPACE and di_active == True:
                        di_input = di_input[:-1]
                    # If the user presses any other key
                    else:
                        if ti_active:
                            ti_input += event.unicode
                        elif di_active and event.key != pygame.K_TAB:
                            di_input += event.unicode

        # Wrong input format or out of range
        if int_error == True or ti_len_error == True or di_len_error == True:
            # Clears input boxes
            ti_input = ''
            di_input = ''
            ti_active = True
            ti_colour = colour_active
            di_active = False
            di_colour = colour_inactive
            if int_error == True:
                text_error = text_format("Please input a whole number.", font, smaller_font, red)
            elif ti_len_error == True:
                text_error = text_format("Please input a whole number between 1 and 599 minutes.", font, smaller_font, red)
            elif di_len_error == True:
                text_error = text_format("Please input a whole number between 200 and 20000 metres.", font, smaller_font, red)
            # Revert boolean variable to prevent the input boxes always resetting
            int_error = False
            ti_len_error = False
            di_len_error = False
            display_error = True

        # Fill background
        screen.fill(light_grey)

        # Display error message if input is incorrect
        if display_error == True:
            error_rect = text_error.get_rect()
            error_background = pygame.Rect(screen_width * 0.19, screen_height * 0.57, 600, 40)
            pygame.draw.rect(screen, white, error_background, 0)
            screen.blit(text_error, (error_background.x + (error_background[2] - error_rect[2]) / 2, error_background.y + (error_background[3] - error_rect[1]) / 4))

        # Drawing input box description, input box and log in/sign up buttons
        text_time = text_format("Time (minutes):", font, small_font, white)
        text_duration = text_format("Distance (metres):", font, small_font, white)
        text_log = text_format("Timed Row", font, small_font, white)
        text_sign = text_format("Distance Row", font, small_font, white)
        un_rect = text_time.get_rect()
        pw_rect = text_duration.get_rect()
        log_rect = text_log.get_rect()
        sign_rect = text_sign.get_rect()
        pygame.draw.rect(screen, ti_colour, time_input_box, 0)
        pygame.draw.rect(screen, di_colour, distance_input_box, 0)
        pygame.draw.rect(screen, blue, time_button, 0)
        pygame.draw.rect(screen, blue, distance_button, 0)
        screen.blit(logo_img, (screen_width / 2 - (logo_dimensions[0] / 2), screen_height * 1 / 40))
        screen.blit(text_time, (time_input_box.x - un_rect[2], time_input_box.y))
        screen.blit(text_duration, (distance_input_box.x - pw_rect[2], distance_input_box.y))
        screen.blit(text_log, (time_button.x + (time_button[2] - log_rect[2]) / 2, time_button.y + (time_button[3] - log_rect[1]) / 4))
        screen.blit(text_sign, (distance_button.x + (distance_button[2] - sign_rect[2]) / 2, distance_button.y + (distance_button[3] - sign_rect[1]) / 4))
        # Render the text
        time_txt_surface = font.render(ti_input, True, black)
        distance_txt_surface = font.render(di_input, True, black)
        # Resize the box if the text is too long
        time_width = max(110, time_txt_surface.get_width() + 10)
        time_input_box.w = time_width
        distance_width = max(110, distance_txt_surface.get_width() + 10)
        distance_input_box.w = distance_width
        # Blit the text
        screen.blit(time_txt_surface, (time_input_box.x, time_input_box.y))
        screen.blit(distance_txt_surface, (distance_input_box.x, distance_input_box.y))
        # Render 'Back' button
        text_back = text_format("BACK", font, small_font, white)
        back_rect = text_back.get_rect()
        back_button = pygame.Rect(back_rect.x + screen_width / 20, screen_height / 1.15, 120, 50)
        pygame.draw.rect(screen, blue, back_button, 0)
        screen.blit(text_back, (back_button.x + (back_button[2] - back_rect[2]) / 2, back_button.y + (back_button[3] - back_rect[1]) / 4))
        pygame.display.flip()
        clock.tick(30)

# Displays averages of each data item from each workout from the user
def stats():

    #Initialises variables
    store_user_pace = []
    store_user_duration = []
    store_user_distance = []
    store_user_cadence = []
    store_user_calories = []
    store_user_power = []
    store_user_heartrate = []
    i = 0

    global user
    # Averages each column in the user's workout file
    def user_average(store_user, i):
        with open('user_' + (str(user) + '.csv')) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ',')
            headers = next(csv_reader)
            for row in csv_reader:
                store_user.append(float(row[i]))
        avg_user = sum(store_user) / len(store_user)
        return avg_user

    avg_user_pace = user_average(store_user_pace, 0)
    avg_user_pace_formatted = str((datetime.timedelta(seconds = avg_user_pace)))[3:7]
    avg_user_duration = user_average(store_user_duration, 1)
    avg_user_duration_formatted = str((datetime.timedelta(seconds = avg_user_duration)))[3:7]
    avg_user_distance = str(user_average(store_user_distance, 2))
    avg_user_cadence = str(user_average(store_user_cadence, 3))
    avg_user_calories = str(user_average(store_user_calories, 4))
    avg_user_power = str(user_average(store_user_power, 5))
    avg_user_heartrate = str(user_average(store_user_heartrate, 6))
    total = str(len(store_user_pace))

    viewing = True

    # While the user is viewing the screen, render the data to the screen
    while viewing == True:

        screen.fill(light_grey)

        title = text_format(user + "'s STATISTICS", font, large_font, white)
        title_rect = title.get_rect()
        screen.blit(title, (screen_width / 2 - title_rect[2] / 2, screen_height / 20))

        text_avg_user_pace = text_format("Average Pace per Workout:  " + avg_user_pace_formatted, font, small_font, white)
        avg_user_pace_rect = text_avg_user_pace.get_rect()
        screen.blit(text_avg_user_pace, (avg_user_pace_rect.x + screen_width / 20, screen_height / 6))

        text_avg_user_duration = text_format("Average Time Rowed per Workout:  " + avg_user_duration_formatted, font, small_font, white)
        avg_user_duration_rect = text_avg_user_duration.get_rect()
        screen.blit(text_avg_user_duration, (avg_user_duration_rect.x + screen_width / 20, screen_height / 6 + avg_user_duration_rect[3] * 2))

        text_avg_user_distance = text_format("Average Distance Rowed per Workout:  " + avg_user_distance + "m", font, small_font, white)
        avg_user_distance_rect = text_avg_user_distance.get_rect()
        screen.blit(text_avg_user_distance, (avg_user_distance_rect.x + screen_width / 20, screen_height / 6 + avg_user_distance_rect[3] * 4))

        text_avg_user_cadence = text_format("Average cadence per Workout:  " + avg_user_cadence + " S/M", font, small_font, white)
        avg_user_cadence_rect = text_avg_user_cadence.get_rect()
        screen.blit(text_avg_user_cadence, (avg_user_cadence_rect.x + screen_width / 20, screen_height / 6 + avg_user_cadence_rect[3] * 6))

        text_avg_user_calories = text_format("Average calories Burnt per Workout:  " + avg_user_calories, font, small_font, white)
        avg_user_calories_rect = text_avg_user_calories.get_rect()
        screen.blit(text_avg_user_calories, (avg_user_calories_rect.x + screen_width / 20, screen_height / 6 + avg_user_calories_rect[3] * 8))

        text_avg_user_power = text_format("Average power per Workout:  " + avg_user_power + "W", font, small_font, white)
        avg_user_power_rect = text_avg_user_power.get_rect()
        screen.blit(text_avg_user_power, (avg_user_power_rect.x + screen_width / 20, screen_height / 6 + avg_user_power_rect[3] * 10))

        text_avg_user_heartrate = text_format("Average Heart Rate per Workout:  " + avg_user_heartrate + " B/M", font, small_font, white)
        avg_user_heartrate_rect = text_avg_user_heartrate.get_rect()
        screen.blit(text_avg_user_heartrate, (avg_user_heartrate_rect.x + screen_width / 20, screen_height / 6 + avg_user_heartrate_rect[3] * 12))

        text_total = text_format("Number of Workouts: " + total, font, small_font, white)
        total_rect = text_total.get_rect()
        screen.blit(text_total, (total_rect.x + screen_width / 20, screen_height / 6 + total_rect[3] * 14))

        # Render the 'back' button
        text_back = text_format("BACK", font, small_font, white)
        back_rect = text_back.get_rect()
        back_button = pygame.Rect(back_rect.x + screen_width / 20, screen_height / 1.15, 120, 50)
        pygame.draw.rect(screen, blue, back_button, 0)
        screen.blit(text_back, (back_button.x + (back_button[2] - back_rect[2]) / 2, back_button.y + (back_button[3] - back_rect[1]) / 4))

        # Handles the mouse clicks by the user
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                #click()
                viewing = False
            if event.type == pygame.K_SPACE:
                viewing = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Return to the main menu when the user clicks the back button
        if viewing == False:
            main_menu()

        pygame.display.update()
        clock.tick(FPS)

log_in()
pygame.quit()
quit()