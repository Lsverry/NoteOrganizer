# Note Organizer

Note Organizer is a web application designed to help users create, view, edit, and delete notes. It also includes user authentication features such as registration and login.

## Features
- User registration and login
- Create, view, edit, and delete notes
- Search notes
- User authentication and authorization
- Responsive design

## Technologies Used

- **HTML5**
- **CSS3**
- **Python**
- **Django**
- **Bootstrap**

## UX Design Documentation
## wireframes
1. **Home Page Wireframe**:
    - **Description**: This wireframe shows the initial structure of the home page, including the navigation bar, register button, and login button.
    - ![Home Page Wireframe]()

2. **Notes List Wireframe**:
    - **Description**: This wireframe illustrates the page where users can view a list of their notes. It includes buttons to create, edit, and delete notes.
    - ![Notes List Wireframe]()

3. **Note Detail Wireframe**:
    - **Description**: This wireframe shows the detail page for a specific note, with options to edit or delete the note.
    - ![Note Detail Wireframe]()

## Design Rationale

1. **Interface Consistency**:
    - **Description**: The user interface has been designed to maintain a consistent look and feel throughout the application. This includes the use of consistent colors, fonts, and styles to enhance usability and user experience.

2. **Ease of Use**:
    - **Description**: Ease of use has been prioritized, ensuring that the main actions (creating, editing, and deleting notes) are easily accessible and understandable for users.

3. **Accessibility**:
    - **Description**: The design has considered accessibility guidelines to ensure that all users, including those with disabilities, can use the application effectively.

## Implementation

1. **Following Wireframes**:
    - **Description**: Wireframes have been closely followed during development to ensure the final product aligns with the initial design vision.

2. **Technical Implementation**:
    - **Description**: The technical implementation has adhered to the established design principles, ensuring the user interface is intuitive and easy to use.

## Testing

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
- Authentication: Verification of user registration, login, and protected access


## Deployment