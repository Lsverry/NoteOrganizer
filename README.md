# Note Organizer

Note Organizer is a web application designed to help users create, view, edit, and delete notes. It also includes user authentication features such as registration and login.

## Features
- User registration and login
- Create, view, edit, and delete notes
- Search notes
- User authentication and authorization
- Responsive design

## User Stories
The following user stories were used to guide the development of the Note Organizer application:

1. **User Registration**: As a user I can register so that I can access the application.
2. **User Login**: As a user I can log in so that I can access my notes.
3. **Create Note**: As a user I can create a new note so that I can save important information.
4. **Note Detail View**: As a user I can view the details of a note so that I can read its content.
5. **Edit Note**: As a user I can edit an existing note so that I can update its content.
6. **Delete Note**: As a user I can delete a note that I no longer need.
7. **Search Notes**: As a user I can search for notes so that I can quickly find specific information.

These user stories are also documented and tracked in the agile tool, GitHub Projects.

## UX Design Documentation

### Entity Relationship Diagram
This application uses a relational database to store user information and notes. The main models are User and Note.

![Entity Relationship Diagram](static/images/Entity%20diagram.png)

### Design
- Colour Scheme
    - The main colour used in the project is white.
- Fonts
    - The fonts used are those predefined by bootstrap.

### Wireframes
1. **Home Page Wireframe**:
    - **Description**: This wireframe shows the initial structure of the home page, including the navigation bar, register button, and login button.
    ![Home Page Wireframe](static/images/Home%20wireframe.png)

2. **Notes List Wireframe**:
    - **Description**: This wireframe illustrates the page where users can view a list of their notes. It includes buttons to create, edit, and delete notes.
    ![Notes List Wireframe](static/images/Note%20list%20wireframe.png)

3. **Create Note Wireframe**:
    - **Description**: This wireframe shows the notes creation page, with a text field for the title, a text field for the content and a save button.
    ![Create Note Wireframe](static/images/Create%20note%20wireframe.png)

3. **Edit Note Wireframe**:
    - **Description**: This wireframe shows the notes edit page, with a text field for the title, a text field for the content and a save button.
    ![Edit Note Wireframe](static/images/Note%20edit%20wireframe.png)

4. **Search Notes Wireframe**:
    - **Description**: This wireframe shows the note search page, with a text field and a button to search for notes.
    ![Search Notes Wireframe](static/images/search%20wireframe.png)

5. **Note detail Wireframe**:
    - **Description**: This wireframe illustrates the notes detail page, with a button to edit it and a button to return to the notes list.
    ![Note detail Wireframe](static/images/Note%20detail%20wireframe.png)

### Screenshots

These are the screenshots of the finished project:

1. **Home Page**
    - **Description**: This is the main page of the Note Organizer application. Users can browse to view their notes or sign up for a new account.
    ![Home Page](static/images/home%20page%20sc%202.png)
2. **Notes List**
    - **Description**: This page displays a list of all notes created by the logged-in user. Users can view, edit, or delete their notes from this page.
    ![Notes List](static/images/Note%20list%20sc%202.png)
3. **Create Note**
    - **Description**: The note creation page where users can enter a title and content for a new note. The form includes input fields for the title and content, and a save button to submit the new note.
    ![Create note](static/images/Create%20Note%20sc%202.png)
4. **Edit Note**
    - **Description**: This page allows users to edit an existing note. It pre-fills the form with the current title and content of the note. Users can make changes and save them.
    ![Edit note](static/images/Edit%20note%20sc%202.png)
5. **Search Results**
    - **Description**: The search page enables users to search for notes by keywords. It includes a search input field and a button to initiate the search.
    ![Search Notes](static/images/search%20results%20sc%202.png)
6. **Registration Form**
    - **Description**: The user registration form where new users can create an account by providing a username and password. It includes input fields for the required information and a submit button to complete the registration.
    ![Registration Form](static/images/Register%20sc%202.png)
7. **Log In Form**
    - **Description**: The login form for returning users to access their accounts. It includes input fields for the username and password, along with a login button.
    ![Log in form](static/images/login%20sc%202.png)
8. **Note Detail**
    - **Description**: This page displays the details of a specific note. Users can see the title and content of the note, and have options to edit the note or go back to the list of notes.
    ![Note Detail](static/images/Note%20detail%20sc%202.png)

### Design Rationale
1. **Interface Consistency**:
    - The user interface has been designed to maintain a consistent look and feel throughout the application. This includes the use of consistent colors, fonts, and styles to enhance usability and user experience.

2. **Ease of Use**:
    - Ease of use has been prioritized, ensuring that the main actions (creating, editing, and deleting notes) are easily accessible and understandable for users.

3. **Accessibility**:
    - The design has considered accessibility guidelines to ensure that all users, including those with disabilities, can use the application effectively.

### Implementation
1. **Following Wireframes**:
    - Wireframes have been closely followed during development to ensure the final product aligns with the initial design vision.

2. **Technical Implementation**:
    - The technical implementation has adhered to the established design principles, ensuring the user interface is intuitive and easy to use.

## Technologies Used

### Languages Used
- **HTML5**
- **CSS3**
- **Python**

### Frameworks and Libraries
- **Django**
- **Bootstrap 4.5.2**
- **Django Allauth**
- **Whitenoise**
- **dj-database-url**
- **python-decouple**
- **gunicorn**
- **psycopg2**

## Tools and Programs
- **Git**
- **GitHub**
- **GitHub Projects**
- **Heroku**
- **VS Code**
- **PostgreSQL**
- **SQLite**
- **Draw.io**
- **figma**
- **Pylint**

## Testing
### Performance
The website was tested with the Lighthouse tool from the developer tools. These are the results from the different pages:

**Home Page:**

![Home Page](static/images/home%20performance%20100.png)

**Note List:**

![Note List](static/images/My%20notes%20performance%20100.png)

**Search Results:**

![Search Results](static/images/search%20results%20performance%2099.png)

**Create Note:**

![Create Note](static/images/create%20note%20performance%20100.png)

**Edit Note:**

![Edit Note](static/images/edit%20note%20performance%20100.png)

**Login Page:**

![Login Page](static/images/Login%20performance%20100.png)

**Register Page:**

![Register Page](static/images/Register%20performance%20100.png)

### Code Validation
#### HTML
The HTML code was validated using the [W3C Markup Validator](https://validator.w3.org/). The validator reported errors related to Django template tags (e.g., `{% block content %}`, `{% url 'note_list' %}`). These errors are expected and do not affect the functionality of the site as they are specific to Django's templating language.

#### CSS
The CSS code was validated using the  [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/). These are the results:

![Results](static/images/css%20results.png)

#### Python
The Python code was checked with Pylint to ensure it adheres to the coding standards. The Pylint score achieved was 10.00/10, indicating no issues were found in the code.
![Pylint](static/images/pylint%20rate.png)

### JavaScript
This project does not include custom JavaScript.

### Automated Testing
The following automated tests have been implemented and passed using Django's testing framework:

1. **Model Tests**
   - **Note Creation**: Verifies that a note can be created with a specific title and content associated with a user.

2. **View Tests**
   - **Note List View**: Verifies that the note list view displays all notes for the authenticated user.
   - **Note Detail View**: Verifies that the detail view of a note shows the correct note information.
   - **Note Creation**: Verifies that a new note can be created and that the application redirects correctly after creation.
   - **Note Update**: Verifies that an existing note can be updated and that the application redirects correctly after the update.
   - **Note Deletion**: Verifies that an existing note can be deleted and that the application redirects correctly after deletion.
   - **Note Search**: Verifies that the note search functionality works correctly.

### Manual Testing
In addition to automated tests, the following manual tests have been performed to verify the usability and responsiveness of the application:

1. **User Registration and Login**
   - Registration of new users.
   - Login of registered users.
   - Verification of access to protected functionalities only after logging in.

2. **User Interface**
   - Navigation through different sections of the application.
   - Verification of design consistency and accessibility.

3. **Responsiveness**
   - Verification of proper display and functionality of the application on different devices and screen sizes.
   - Ensuring that navigation bar buttons are visible and functional on mobile devices.

4. **Cross-Browser Testing**
   - The application was tested on different web browsers to ensure compatibility and consistent performance. Browsers tested include:
     - Google Chrome
     - Mozilla Firefox
     - Microsoft Edge
     - Safari

### Frameworks and Tools Used
- **Django's Testing Framework**: Used for implementing and running automated tests.

### Running the Tests
To run the automated tests, follow these steps:

1. **Set up the environment**:
    Ensure that all dependencies are installed and the database is migrated.
    ```bash
    pip install -r requirements.txt
    python manage.py migrate
    ```

2. **Run the tests**:
    ```bash
    python manage.py test
    ```

### Test Coverage
- Models: Verification of the Note model creation.
- Views: Verification of CRUD operations and search functionality for notes.
- Authentication: Verification of user registration, login, and protected access.

### User Stories Testing
- User Registration: As a user I can register so that I can access the application:
    - The user can click on Register in the navigation bar or on the home page to create an account with a username and password.

- User Login: As a user I can log in so that I can access my notes:
    - The user can click on Login in the navbar to access their account by entering their credentials.

- Create Note: As a user I can create a new note so that I can save important information:
    - The user can click on "Create note" in the "my notes" section to access the note creation form and save a new note.

- Note Detail View: As a user I can view the details of a note so that I can read its content:
    - The user can click on a note title in the notes list to view its details on a separate page.

- Edit Note: As a user I can edit an existing note so that I can update its content:
    - The user can click on the "Edit" button on the note detail page to update the note's content.

- Delete Note: As a user I can delete a note that I no longer need:
    - The user can click on the "Delete" button on the note detail page to remove the note.
    
- Search Notes: As a user I can search for notes so that I can quickly find specific information:
    - The user can enter a keyword in the search bar and click the search button to find notes that contain the keyword in their title or content.

## Known Bugs

### Resolved Bugs

1. **Logout not working correctly**:
    - **Description**: Initially, the logout functionality was causing a 405 error due to incorrect URL pattern and template settings.
    - **Solution**: The URL pattern was corrected and the template settings were properly configured to handle logout requests.
2. **Form field alignment issues**:
    - **Description**: Form fields for creating and editing notes were not aligned properly.
    - **Solution**: Custom template tags were created to add CSS classes to form fields for proper alignment.
3. **Display of note content**:
    - **Description**: When viewing the details of a note, line breaks in the note content were not being displayed correctly.
    - **Solution**: The `linebreaks` filter was used in the template to preserve line breaks in note content.
4. **Registration button visible when logged in**:
    - **Description**: The registration button was still visible in the navigation bar even when the user was logged in.
    - **Solution**: Added conditional logic in the base template to hide the registration button when the user is authenticated.
5. **Search Notes without Login causing 500 error**:
    - **Description**: Searching for notes without being logged in was causing a 500 server error.
    - **Solution**: The `search_notes` view was updated to check if the user is authenticated and handle the search accordingly.
6. **Navigation Bar Buttons not visible on Mobile Devices**:
    - **Description**: The navigation bar buttons (Login, Search Notes, Logout, etc.) were not visible on mobile devices.
    - **Solution**: The navigation bar was updated to include a toggler for mobile view, ensuring all buttons are accessible on smaller screens.

### Unfixed Bugs
No unfixed bugs.

## Deployment

### Heroku
- The App live link is: 
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App.
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

### Fork the Repository
1. Log in to GitHub: Ensure you are logged in to your GitHub account.
2. Navigate to the Original Repository: Go to the original repository of the project you want to fork.
3. Fork the Repository:
    - In the top right corner of the repository page, click the Fork button.
    - GitHub will create a copy of the repository under your account.
4. Verify the Fork: Once the fork is complete, you will be redirected to the copy of the repository in your GitHub account.

### Clone the Repository
1. Navigate to Your Forked Repository: Go to the forked repository in your GitHub account.
2. Get the Repository URL:
    - Click on the green Code button.
    - Copy the repository URL. 
3. Open Terminal or Command Prompt: Open your terminal (macOS, Linux) or command prompt (Windows).
4. Clone the Repository:
    - Navigate to the directory where you want to clone the repository.
    - Run the following command, replacing REPOSITORY_URL with the URL you copied:
    ```bash
    git clone REPOSITORY_URL
    ```
5. Navigate to the Project Directory:
    - After the repository is cloned, navigate to the project directory:
    ```bash
    cd repository_name
    ```
6. Install Dependencies:
    - Ensure you have all necessary dependencies installed. You can do this by running:
    ```bash
    pip install -r requirements.txt
    ```
7. Migrate the Database:
    - Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```
8. Run the Server:
    - Start the Django development server:
    ```bash
    python manage.py runserver
    ```

## Future Implementations
- Improve the search functionality to include advanced search options.
- Add a feature for users to categorize their notes.
- Enhance the user interface for a more modern look and feel.
- Implement additional security features for user data protection.

## Credits
- **Acknowledgements**: Special thanks to the Django and Bootstrap communities for their excellent documentation and resources.
- **Favicon**: [Font Awesome](https://fontawesome.com/)