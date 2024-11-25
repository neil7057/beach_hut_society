# My Beach Hut Appreciation Society Website

![Mockup](docs/readme_images/site_mockup.jpg)

**Author Neil Allen**

## Beach Hut Appreciation Society

This is my website. It's a bit of fun to demonstrate capability in CRUD functionality. It's a website forum for beach hut aficianados and utilises Bootstrap and Flask and a Postgres Sql Dtabase. Written in HTML, CSS and Python following a common approach to data structures supporting similar applications. 

[View the live project here.](https://beach-hut-appreciation-society-0c8700c133d2.herokuapp.com/)

# Table of Contents

1. [Project Inception and Planning](#project-inception-and-planning)
2. [Overview](#overview)
3. [User Experience (UX)](#user-experience-ux)
    *   [User stories](#user-stories)
        *   [First Time Visitor Goals](#first-time-visitor-goals)
        *   [Returning Visitor Goals](#returning-visitor-goals)
        *   [Frequent User Goals](#frequent-user-goals)
    *   [Design](#design)
        *   [Colour Scheme](#colour-scheme)
        *   [Typography](#typography)
        *   [Imagery](#imagery)
        *  [Design Considerations](#design-considerations)
    *   [Database Design](#database-design)
        *   [Table Struture](#table-structure)
        *   [Diagram](#diagram)
    *   [Wireframes](#wireframes)
        *   [Base Template](#base)
        *   [Home](#home)
            *   [Logged In](#logged-in)
            *   [Logged Out](#logged-out)
        *   [Sign Up](#sign-up)
        *   [Log In](#log-in)
        *   [About](#about)
        *   [Contact](#contact)
        *   [Edit Profile](#edit-profile)
        *   [Edit Profile - Admin](#edit-profile---admin)
        *   [View Full Post Page](#view-full-posts-page)
        *   [Posts](#posts)
            *   [Create Post](#create-a-new-post)
            *   [Edit Post](#edit-post)
            *   [Delete Post](#delete-post)
        *   [Comments](#comments)
            *   [Add Comment](#add-comment)
            *   [Edit Comment](#edit-comment)
            *   [Delete Comment](#delete-comment)
        *   [Add Tag](#add-tag)
        *   [Manage Users](#manage-users)
        *   [Manage Contacts](#manage-contacts)
        *   [Search Results](#search-results)
    *   [Structure](#structure)
4. [Features](#features)
5. [Pages](#pages)
    *   [Landing Page](#landing-page)
        *   [Menu Bar Logged Out](#menu-bar---logged-out)
        *   [Menu Bar Logged User](#menu-bar---logged-in)
        *   [Menu Bar Logged Admin](#menu-bar---admin)
        *   [Floating Anchor](#floating-anchor)
    *   [Sign Up Page](#sign-up-page)
    *   [Log in Page](#log-in-page)
    *   [About Page](#about-page)
    *   [My Posts Page](#my-posts-page)
    *   [Edit Profile Page](#edit-profile-page)
    *   [Edit Profile - Admin Page](#edit-profile---admin-page)
    *   [View All Posts Page](#view-all-posts-page)
    *   [Post Pages](#posts-pages)
        *   [Create Post](#create-post-page)
        *   [Edit Post](#edit-post-page)
        *   [Delete Post](#delete-post-page)
    *   [Comments Pages](#comments-pages)
        *   [Create Post](#create-comment-page)
        *   [Edit Post](#edit-comment-page)
        *   [Delete Post](#delete-comment-page)
    *   [Tag Pages](#tag-pages)
        *   [Create Tag](#create-tag-page)
        *   [Browse Tags](#browse-all-tags-page)
        *   [Delete Tag](#delete-tag-page)
    *   [Manage Users](#manage-users-page)
    *   [Manage Contacts](#manage-contacts-page)
    *   [Search Results](#search-results-page)
    *   [Contact Page](#contact-page)
    *   [Flash Messages](#flash-messages)
    *   [Site Features](#site-features)
6. [Technologies Used](#technologies-used)
    *   [Development Environment](#development-environment)
    *   [Languages Used](#languages-used)
    *   [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
7. [Testing](#testing)
    *   [HTML](#html)
    *   [CSS](#css)
    *   [JavaSceipt](#javascript)
    *   [PeP8](#pep8)
    *   [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
        *   [First Time Visitor Goals](#first-time-visitor-goals-1)
        *   [Returning Visitor Goals](#returning-visitor-goals-1)
        *   [Frequent User Goals](#frequent-user-goals-1)
    *   [Responsiveness](#responsiveness)
    *   [Accessibility](#accessibility)
    *   [Screen Reader](#screen-reader)
    *   [Lighthouse Testing](#lighthouse-testing)
    *   [Functional Testing](#functional-testing)
        *   [Navigation Links](#navigation-links)
        *   [Testing Approach](#testing-approach)
        *   [Test Accounts](#test-accounts)
        *   [Sign Up](#sign-up-testing)
        *   [Log In](#log-in-testing)
        *   [Thread Post](#thread-post-testing)
        *   [Comments](#comments-testing)
        *   [Tags](#tags-testing)
        *   [Manage Users](#manage-users-testing)
        *   [Search Function](#search-function-testing)
        *   [Contact](#contact-testing)   
        *   [Links Testing](#links-testing)
        *   [Footer Contact Information](#footer-contact-information)
    *   [Further Testing](#further-testing)
    *   [Bugs and Fixes](#bugs-and-fixes)
    *   [Known Bugs](#known-bugs)
    *   [Future Releases](#future-releases)
8. [Deployment](#deployment)
    *   [Version control](#version-control)
    *   [Github Pages](#github-pages)
    *   [Deployments to Github Pages](#deployment-to-github-pages)
    *   [Clone the repository locally](#clone-the-repository-code-locally)
    *   [Heroku](#heroku)
    *   [App Deployment](#app-deployment-to-heroku)
9. [Credits](#credits)
    *   [Code](#code)
    *   [Content](#content)
    *   [Media](#media)
    *   [Acknowledgements](#acknowledgements)

## Project Inception and Planning

## Overview

The website is a Blog site for lovers of Beach Huts. anonymous visitors can read the About page, search by keyword, send a Contact message and view the latest posts and latest comment. To access the full posts and additional comments or to post or comment on a post, Visitors must sign-up using their email address and then Login.

Logged in users can view all posts and comments and create new posts and comments and category Tags. Logged in users can edit and delete their own posts and can edit and delete their own comments whether on their own post or someone elses.

Logged in users can list their own posts and comments and can edit basic user details. They cannot delet thier account as that would remove posts and comments and i decided that contnet should remain - unless its offensive.

Administrators can post, edit and delete their own threads and comments as per normal users but additionally can:
-   Delete Tags
-   Delete Contact records
-   Edit user accounts to change the main entries
-   Reseet a user's password
-   Toggle User status between normal/admin
-   Delete the User account should it be deemed necessary

Administrators can also review and delete contact messages.

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to see what the site is about.
        2. As a First Time Visitor, I want to get an indictaion of the types of content. 
        3. As a First Time Visitor, I want to be able to sign up and post.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to log in and view posts.
        2. As a Returning Visitor, I wannt to see a list of the latest forum posts.
        3. As a Returning Visitor, I want to be able to view all my posts.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to be able to search for on topic content by keyword.
        2. As a Frequent User, I want to be abe to manage my account settings.
        3. As a Frequent User, I want to be able to post and comment on my and other threads.

-   ### Design
    -   #### Colour Scheme
        -   I've used the pastel beach themed colours to reflect the subject matter of the site. A pale blue (#C8E4FD) background for the body.
        Titles alternatively in Dark Blue (#4203BF) and Sand (#AA4313) with text in Light Blue and Sand. Buttons are consistent according to function.
        -   General navigation buttons are similarly styled and edit, comment and delete buttons are styled differently to differentiate but remain consistnet amongst the forum post and tag elements.
        -   Some colours were muted or changed to meet WAVE guidelines during final stage testing. 
        
    -   #### Typography
        -   The fonts chosen are Original Surfer and Seaweed Script to adhere to the beach theme. Seaweed Script is novel and suitable for titles  but unsuitable for use in large text blocks as it can make it difficult to read. Sans-serif is the fallback font.
 
    -   #### Imagery
        -   There is a Hero image in the base template which propogates to each page and gives the site a consistenmt look and feel.
        -   There is a beach logo on larger screens but is hidden below 1000px.
        -   The site has a couple of additional images on the About page but as a blog site is mostly text based, for now..

    -   #### Design Considerations
        -   The site is built with templates based on Base.html so retains a consistent Header and Footer
     
        -   Colours are Bold yet soft and are selected to communicate a fun, beach theme and reflect the varied colours that are common to beach hut installations.

        -   The header and footer occupy the whole width of the screen but content has wide margins on larger screen sizes with thin margins for tablet and mobile views.

        -   The site is responsive with menus and text resized for smaller screens. 

        -   Menu navigation is consistent across all pages and screen sizes and is central to each page. Menus change according to login and admin status.

        -   Menu button text is Sand with a yellow background. The admin only function is highlighted in Green.

        -   There are popup confirmations on all Delete functions and each update page also offers a 'cancel' function rather than expecting the user to use tha back button or actively click elsewhere.

        -   Administrators have additional functions which are presented when they access different areas of the site.

        -   Error and confirmation messages are displayed at the top of the main site area, below the secondary menus. I chose not to make these disappear automatically or after a stated time as I personally find that inconvenient and prefer to have messages displayed until I have read that at my pace and taken action to dismiss them.
        
        -   Threads(posts) and the first comment are visible to all visitors but users have to register and login to see full posts, full comments or be able to post or comment.

        -   Logged in users get to see their user profile, can edit it and can see all their own posts on a 'view all posts' page. I chose not to allow users to delete their own accounts as that would remove content from the site, incluidng any responses from other users. 

-   ### Database Design
-   #### Table Structure
    *   A User Table with unique ID. User information. 
    *   A Thread Table with unique ID. Essentially a forum post, linked to a User.
    *   A Comments Table with unique ID. A comment or comments, attached to Thread and linked to the User who posted the comment, not necessarilly the same user who posted the thread.
    *   A Tag Table with unique ID. A category that can be attached to a post to assist with searches. 
    *   A Thread-Tag Table to resolve the Many-to-Many relationship between Tags and Threads.
    *   A Contact Table with unique ID. Holds messages for admin review and processing.

-   #### Diagram
    <details><summary>Data Structure</summary>
    <img src="beachhuts/static/docs/table_layout.png">
    </details>

-   ### Wireframes
    -   Many functions are repetitive so create, edit and delete are basically similar for different record types.
    -   It wasn't necessary therefore to wireframe all proposed images and I chose to create a template for each distinct function.
    -   Developemnt was then iterative and Agile.
-   #### Base
    <details><summary>Base Template</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/base-html.png">
    </details>

-   #### Home
-   ##### Logged In
    <details><summary>Home - Logged In</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/home-logged-in.png">
    </details>

-   ##### Logged Out
    <details><summary>Home - Logged Out</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/home-logged-out.png">
    </details>
    
-   #### Sign Up
    <details><summary>Sign Up</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/signup.png">
    </details>

-   #### Log In
    <details><summary>Log In</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/login.png">
    </details>

-   #### About
    <details><summary>About</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/about.png">
    </details>

-   #### Contact
    <details><summary>Contact</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/contact.png">
    </details>

-   #### Edit Profile
    <details><summary>Edit profile</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/edit-profile.png">
    </details>

-   #### Edit Profile - Admin
    <details><summary>Edit profile, Administrator</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/edit-profile-admin.png">
    </details>

-   #### View All Posts For User
    <details><summary>View All posts For A User</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/my-threads.png">
    </details>

-   #### Posts
-   ##### Create A New Post
    <details><summary>Create A New Post</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/Create-post.png">
    </details>

-   ##### Edit Post
    <details><summary>Edit post</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/Edit-post.png">
    </details>

-   ##### Delete Post
    <details><summary>Delete post</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/delete-post.png">
    </details>

-   #### Comments
-   ##### Add Comment
    <details><summary>Add Comment</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/add-comment.png">
    </details>

-   #### Edit Comment
    <details><summary>Edit Comment</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/edit-comment.png">
    </details>

-   #### Delete Comment
    <details><summary>Delete Comment</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/delete-comment.png">
    </details>

-   #### Add tag
    <details><summary>Add Tag</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/tags.png">
    </details>

-   #### Manage Users
    <details><summary>Manage Users</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/manage-users.png">
    </details>

-   #### Manage Contacts
    <details><summary>Manage Contacts</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/search-resultsmanage-contacts.png">
    </details>

-   #### Search Results 
    <details><summary>Search Results</summary>
    <img src="beachhuts/static/docs/readme_images/wireframes/search-results.png">
    </details>
 
-   ### **Structure**

    The structure of the site is informed by the the target audience's expectations and the principles of IXD (interaction design) to make sure I was making everything as intuitive as I could. Each page has a clear function and is named to give a clear indication of content/function.

    Visitors can view some site content but to add or view full content, visitors are required to sign up and login.

    Functions serve:
    -   Sign Up
    -   Login and out
    -   Thread(Post) full view, creation, edit, deletion
    -   Comment creation, edit and deletion
    -   Category tag creation and deletion
    -   An About Page
    -   Admin functions to manage Users and edit/delete all elements
    -   User profile editing
    -   Contact/feedback Form
    -   Admin Mangement of contact communications
    -   Search facility

    The site is templated and built around a Base HTML file containing a consistent Header and Footer:

    The site has a navbar which remains central to the screen on desktop, tablet and mobile.

    A second menu bar is presented according to logged in/logged out status. Administrators are presented with additional 'Manage Users' and 'Manage Contacts' button.
    
    There is also a footer on every page with links to social media sites and the Contact page.

    Messages on the Contact page create a database entry for review by Admin, who can delete the records after processing.

    The Hero image is consistent across all pages and there is a search bar. There is a small loogo on larger screens but hidden at smaller resolutions.
    
    Each page has a scrolling 'top of page' anchor link.

    Social media links all point to beach hut specific sites if they exist and standard social channels if not. 

    Permissions to create, update and delete content are determined by user ID, ststus and content craetor ID. 
    
## Features

-   Responsive on all device sizes down to 280px - the industry standard minimum screen width.

## Pages
### Landing Page
-   Landing page image   
    *   The first page is the index or home page.
    *   For visitors, this shows a list of forum posts sorted with most recent first.
    *   For users, this shows the user profile summary plus the list of Forum posts.
    *   This will help to immediately show the visitor/user what the website is about. 
    <details><summary>Landing Page - Visitor</summary>
    <img src="beachhuts/static/docs/readme_images/screens/home-logged-out.png">
    </details>
    <details><summary>Landing Page - User</summary>
    <img src="beachhuts/static/docs/readme_images/screens/home-logged-in.png">
    </details>

-   #### Menu Bar - Logged Out
    <details><summary>Navigation Menu - Logged Out</summary>
    <img src="beachhuts/static/docs/readme_images/screens/menu-logged-out.png">
    </details>

-   #### Menu Bar - Logged In
    <details><summary>Navigation Menu - Logged In User</summary>
    <img src="beachhuts/static/docs/readme_images/screens/menu-logged-in-normal-user.png">
    </details>

-   #### Menu Bar - Admin
    <details><summary>Navigation Menu - Admin</summary>
    <img src="beachhuts/static/docs/readme_images/screens/admin-login.png">
    </details>
    
-   #### Floating Anchor
    Each page also has a floating anchor link at the side to take the user back to the top of the page. 
    <details><summary>Bottom links</summary>
    <img src="beachhuts/static/docs/readme_images/screens/floating.png">
    </details>
    
-   #### Sign Up Page
    Visitors can become a member by registering with their email address and selecting a username and password.
    <details><summary>Sign Up Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/signup.png">
    </details>

-   ####  Log In Page
    <details><summary>Log In Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/login.png">
    </details>

-   #### About Page
    <details><summary>About Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/about.png">
    </details>

-   #### My Posts Page
-   User has no posts and has not commented on any posts.
    <details><summary>My Posts - No Posts</summary>
    <img src="beachhuts/static/docs/readme_images/screens/my-threads-nothing.png">
    </details>
    <br>
-   User has posted and may have commented on posts.
        <details><summary>My Posts - Posts</summary>
    <img src="beachhuts/static/docs/readme_images/screens/my-threads-posts.png">
    </details>
    <br>
-   User has no posts but has commented on other users' posts.
        <details><summary>My Posts - Comments Only</summary>
    <img src="beachhuts/static/docs/readme_images/screens/my-threads-comments-only.png">
    </details>

-   #### Edit profile Page  
    <details><summary>Edit Profile Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/edit-user-profile.png">
    </details>

-   ####  Edit profile - Admin Page
    <details><summary>Edit Profile - Admin Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/edit-user-admin.png">
    </details>

-   #### View Full Posts Page  
    <details><summary>View Full Posts Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/view-thread-full.png">
    </details>

### Posts Pages
-   #### Create Post Page
    <details><summary>Create Post Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/create-a-post.png">
    </details>

-   #### Edit Post Page
    <details><summary>Edit Post Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/edit_thread.png">
    </details>

-   #### Delete Post Page
    <details><summary>Delete Post Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/delete-post-confirm.png">
    </details>

### Comments Pages
-   #### Create Comment Page
    <details><summary>Add Comment Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/add-comment.png">
    </details>

-   #### Edit Comment Page
    <details><summary>Edit Comment Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/edit-comment.png">
    </details>

-   #### Delete Comment Page
    <details><summary>Delete Comment Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/delete-comment-modal.png">
    </details>

### Tag Pages
-   #### Create Tag Page
    <details><summary>Add Tag Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/add-new-tag.png">
    </details>

-   #### Browse All Tags Page
    <details><summary>Browse All Tags (Admin) Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/browse-tags-admin.png">
    </details>

-   #### Delete Tag Page
    Admin only function. Button Hidden for normal users.
    <details><summary>Delete Tag Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/delete_tag.png">
    </details>

### Manage Users Page
* Admin only function. Menu Button Hidden for normal users.
    <details><summary>Manage Users Menu</summary>
    <img src="beachhuts/static/docs/readme_images/screens/admin-manage-users.png">
    </details>

* Admin only function. Menu Button Hidden for normal users.
    <details><summary>Manage Users Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/admin-manage-users2.png">
    </details>

    ### Manage Contacts Page
* Admin only function. Menu Button Hidden for normal users.
    <details><summary>Manage Contacts Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/admin-manage-contacts.png">
    </details>

    <details><summary>Confirmation Dialog</summary>
    <img src="beachhuts/static/docs/readme_images/screens/delete-contact-confirm.png">
    </details>

-   #### Search Results Page
    <details><summary>Search Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/search-results.png">
    </details>

### Contact Page 
* A contact page is offered to allow registered users and non-users to contact me. The form consists of the following fields and attributes: 
    - Username (required, type=text).
    - First Name (required, type=text).
    - Last Name (required, type=text).
    - Email (required, type=email).
    - Message (required, type=textarea), maximum 280 characters.
    - Muted Text is used as hints or for assurance on certain fields. This has been adjusted for WCAG compliance.
* For logged in users, form content is pre-populated with user details from the User table.
* This allows a users and potential users to contact admin with any queries.
* A flash message indicates success or failure of the message send.
* The contact message is stored in a database table for interrogation by admininstrators.

    <details><summary>Contact Page</summary>
    <img src="beachhuts/static/docs/readme_images/screens/contact.png">
    </details>

### Flash Messages
* Flash messages are displayed below the secondary menu bar to notify errors or when a particular creation or edit action has been successful
    <details><summary>Flash Message Example</summary>
    <img src="beachhuts/static/docs/readme_images/screens/flash-message.png">
    </details>

### Site Features

* Responsive design - content scales from 280px to Large Desktop. Some content is hidden at smaller resolutions to maintain user experience.
* Top Menu navbar remains consistent with a secondary Menu bar that responds to user status.
* There is a Top of the Page scrolling button on each page. 
* The main landing page contains a list of posts sorted with most recent first.
* There is an about page to provide more information about the site and the topic 
* Contact form.
* Search facility.
* Sign Up and login functionality.
* Access to Create, Edit and Delete of site elements are controlled by user status and permissions.
* There are links to social media.
* The site is clean and uncluttered and follows a Beach theme.

## Technologies Used

### Development Environment
-   The site was developed in a [Gitpod](https://www.gitpod.io/) environment using VSC.

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://docs.python.org/3/)


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.2.1:](https://getbootstrap.com/docs/4.6.2/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Menu items in the navbar as well as the Social Media icons in the footer to add the 'grow' transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Baskerville Libre' and 'Open Sans' fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Used for icons on social links and drop down menus.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to make the navbar responsive and provide additional coding flexibility. specifically used with the emailJS service, modal and other processing.
1. [Select2:](https://select2.org/)
   - Select2 was used for styling the dropdown to allow multiple selections without CMD/CTRL or Shift.
1. [Gitpod](https://www.gitpod.io/)
   - GitPod was used for version control by utilizing the GitPod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub is used to store the project's code after being pushed from the development environment.
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](#wireframes) during the design process.
1. [Jest:](https://jestjs.io/)
   - Jest was used to test the Javascript used.
1. [SQLAlchemy:](https://docs.sqlalchemy.org/en/20/)
   - SQLAlchemy was used to communicate between the database and the frontend
1. [DBDiagram:](https://dbdiagram.io/home)
   - Used to document database model.
1. [FLASK:](https://flask.palletsprojects.com/)
   - Flask Frameworking was used to structure the site including the use of Jinja2 templating. Allowed for the smooth display of data from the backend. 
1. [StackOverflow:](https://stackoverflow.com/)
    - Used for code snippets and tutorials. Invaluable.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the website to ensure there were no syntax errors in the project.

### HTML

This was carried out periodically as each page was created and amended and then finally checked again when pages were deemed complete and error free.

-   HTML pages are built from a common template (base.html) so cannot be directly scanned by url. Testing was achieved by viewing and copying page source into the validator.

-   Due to the nature of the iterative processing within some pages, errors are generated referring to duplicate IDs. Theses are not genuine errors.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
 
    <details><summary>Home Page</summary>
    <img src="beachhuts/static/docs/testing/ws-home.png">
    </details>
    <details><summary>About Page</summary>
    <img src="beachhuts/static/docs/testing/ws-about.png">
    </details>
    <details><summary>Add Tag Page</summary>
    <img src="beachhuts/static/docs/testing/ws-add-tag.png">
    </details>
    <details><summary>Edit Profile Page</summary>
    <img src="beachhuts/static/docs/testing/ws-edit-user.png">
    </details>
    <details><summary>Manage Users Page</summary>
    <img src="beachhuts/static/docs/testing/ws-manage-users.png">
    </details>
     <details><summary>Edit User Page - Admin</summary>
    <img src="beachhuts/static/docs/testing/ws-edit-user-admin.png">
    </details>
     <details><summary>Manage Contacts - Admin</summary>
    <img src="beachhuts/static/docs/testing/ws-manage-contacts.png">
    </details>
    <details><summary>Contact Page</summary>
    <img src="beachhuts/static/docs/testing/ws-contact.png">
    </details>
    <details><summary>Edit Comment Page</summary>
    <img src="beachhuts/static/docs/testing/ws-edit-comment.png">
    </details>
    <details><summary>Edit Thread Page</summary>
    <img src="beachhuts/static/docs/testing/ws-edit-thread.png">
    </details>
    <details><summary>Login Page</summary>
    <img src="beachhuts/static/docs/testing/ws-login.png">
    </details>
    <details><summary>My Threads Page</summary>
    <img src="beachhuts/static/docs/testing/ws-my-threads.png">
    </details>
    <details><summary>Search Results Page</summary>
    <img src="beachhuts/static/docs/testing/ws-search-results.png">
    </details>
    <details><summary>Sign Up Page</summary>
    <img src="beachhuts/static/docs/testing/ws-signup.png">
    </details>
    <details><summary>Submit Thread Page</summary>
    <img src="beachhuts/static/docs/testing/ws-post-thread.png">
    </details>
    <details><summary>Browse Tags Page</summary>
    <img src="beachhuts/static/docs/testing/ws-browse-tags.png">
    </details>
    <details><summary>View Full Thread Page</summary>
    <img src="beachhuts/static/docs/testing/ws-view-full-thread.png">
    </details>
    
### CSS

This was checked periodically as each page was created and CSS code added and amended. A final check was carried out when all other testing had been satisfactorily completed.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

    <details><summary>style.css</summary>
    <img src="beachhuts/static/docs/testing/ws-style-css-check.png">
    </details>

### JavaScript

This was checked periodically as each page was created and CSS code added and amended. A final check was carried out when all other testing had been satisfactorily completed.

-   [jshint JavaScript Validator](https://jshint.com/)

    <details><summary>Main JS - scripts.js</summary>
    <img src="beachhuts/static/docs/testing/jshint-scripts-js.jpg">
    </details>
### PeP8

This was checked each time substantial changes were made to PY files. A final check was carried out when all other testing had been satisfactorily completed.

-   [PeP8 Python Linter](https://pep8ci.herokuapp.com)

    <details><summary>init.py</summary>
    <img src="beachhuts/static/docs/testing/pep8-init.png">
    </details>
    <br>
    <details><summary>env.py</summary>
    <img src="beachhuts/static/docs/testing/pep8-env.png">
    </details>
    <br>
    <details><summary>models.py</summary>
    <img src="dbeachhuts/static/docs/testing/pep8-models.png">
    </details>
    <br>
    <details><summary>routes.py</summary>
    <img src="beachhuts/static/docs/testing/pep8-routes.png">
    </details>

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals
  
    1. As a First Time Visitor, I want to see what the site is about.
        
        1. The Hero image on the header gives a clear indication of the site's purpose.

        2. There is an About page with further information about the site.

        3. There is a Contact messaging page to ask questions before signup.


    2. As a First Time Visitor, I want to get an indictaion of the types of content. 

        1. The Home page lists the forum threads with most recent first.
        2. The first comment on each post is also displayed.
        3. There is a search facility on the header of each page.

    3. As a First Time Visitor, I want to be able to sign up and post.
       
        1. A link to signup is clearly displayed in the header menu and also in the comments
         on the list of posts. 
        2. Once signed up, buttons are presented for post and comment option 
        3. Once logged in, Post and tag buttons are displayed

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to be able to log in and view posts.
       
        1. The login button is prominently displayed on all pages. 
        2. The post button is prominently displayed and there is an option to comment on all other users' posts.
        3. There is a search facility to find posts by title or category.

    2. As a Returning Visitor, I wannt to see a list of the latest forum posts.

        1. The latest posts are listed on the home page, most recent first.
        2. Each page menu bar has a link to the comments and feedback page where a user can submit a request for more information.

    3. As a Returning Visitor, I want to be able to view all my posts.
       
        1. Once logged in, the Home page shows a summary of the User's account with a button to view all their 
        posts and comments.
        2. There is a search facility to find posts with specific keywords or categories.

-   #### Frequent User Goals

    1. As a Frequent User, I want to be able to search for on topic content by keyword.        
        1. There is a search facility on all pages, located central to the header.
        2. The Search facility will return matches based on post title and content and user name. 

    2. As a Frequent User, I want to be abe to manage my account settings.        
        1. Once logged in, the edit profile button is presented in the account summary as the first
         item on the home page.
        2. The User can amend username, first and last name.
        3. The User can send a message to request password reset or notify a change of email address.
        4. Users can Edit and Delete their own posts and comments via conveniently placed buttons
        on the respective post/comment.

    3. As a Frequent User, I want to be able to post and comment on my and other threads.

        1. Users can create category Tags to attach to posts for ease of searching.
        2. Users can post from the main menu on any page.
        3. Users can comment on their own or other users posts.
        
### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 280px and upwards as defined in [WCAG 2.1 Reflow criteria for responsive design](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html) on the following browsers:
- Chrome    (123.0.6312.106).
- Edge      (123.0.2420.81).
- Firefox   (124.0.2).
- Safari    (17.4).
- Opera     (109.0.5097.24).

Steps to test:

1. Open browser and navigate to:
    - https://beach-hut-appreciation-society-0c8700c133d2.herokuapp.com/
2. Open the developer tools (right click and inspect).
3. Set to responsive and decrease width in stages to 280px.
4. Set the zoom to 50%.
5. Click and drag the responsive window to maximum width, noting transitions at breakpoints.
6. Rotate and test for portrait to landscape transition.

Results:

Website is responsive on all screen sizes and no images are pixelated or stretched.
No horizontal scroll is present.
No elements overlap.
Text resizes as expected at breakpoints.
Some content is hidden where it would clutter smaller screens.

Website was also opened on the following devices and no responsive issues were seen:

- iPhone X, 12, 14.
- Apple iPad 12.9.
- Fujitsu 15.4in laptop.
- Hp 22in desktop.

### Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development
and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs.

- Color contrasts meet a minimum ratio as specified in
  [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).    

- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user.

- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions.

- All non-textual content has alternative text or titles so descriptions are read out to screen readers.

- HTML page lang attribute has been set.

- Aria properties have been implemented correctly.

- WCAG 2.1 Coding best practices being followed.

- Hyperlink text colour has been adjusted to adhere to contrast guidelines.

Results:

Pages that display lists of Posts and comments use the same formatting and colour schemes so it isn't strictly necessary to check all pages with identical contrast and colour components.
-   WCAG results:
    <details><summary>Home Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-home.png">
    </details>
    <details><summary>About Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-about.png">
    </details>
    <details><summary>Contact Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-contact.png">
    </details>
    <details><summary>Signup Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-signup.png">
    </details>
    <details><summary>Login Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-login.png">
    </details>
    <details><summary>Search Results Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-search-results.png">
    </details>
    <details><summary>My Threads Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-my-threads.png">
    </details>
    <details><summary>View Full Thread Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-view-full-thread.png">
    </details>
    <details><summary>Edit User Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-edit-user.png">
    </details>
    <details><summary>Manage Users Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-manage-users.png">
    </details>
    <details><summary>Admin Manage User</summary>
    <img src="beachhuts/static/docs/testing/wcag-edit-user-admin.png">
    </details>
    <details><summary>Manage Contacts Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-manage-contacts.png">
    </details>
    <details><summary>Create Post Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-create-a-post.png">
    </details>
    <details><summary>Edit Post Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-edit-post.png">
    </details>
    <details><summary>Edit Comment Page</summary>
    <img src="beachhuts/static/docs/testing/wcag-edit-comment.png">
    </details>

Manual tests were also performed to ensure the website was as accessible as possible.

### Screen Reader

Screen reader testing was performed using NVDA software from [NV Access](https://www.nvaccess.org/).
This confirmed that:

-   All text is readable.
-   All images have accurate, useful text descriptions.

### Lighthouse Testing
-   The create comment page is a modal and part of submit thread, so testing of that page covers both scenarios.   

    <details><summary>Home Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-home.png">
    </details>
    <br> 
    <details><summary>About Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-about.png">
    </details>
    <br>
    <details><summary>Contact Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-contact.png">
    </details>
    <br>
    <details><summary>Sign Up Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-signup.png">
    </details>
    <br>
    <details><summary>Log In Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-login.png">
    </details>
    <br> 
    <details><summary>Create Post Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-create-post.png">
    </details>
    <br>
    <details><summary>Edit Post Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-edit-post.png">
    </details>
    <br>
    <details><summary>Edit CommentPage</summary>
    <img src="beachhuts/static/docs/testing/ws-light-edit-comment.png">
    </details>
    <br> 
    <details><summary>Browse Tags Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-browse-tags.png">
    </details>
    <br>
    <details><summary>Add Tag Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-add-tag.png">
    </details>
    <br>
    <details><summary>View My Posts Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-my-threads.png">
    </details>
    <br>
    <details><summary>View Full Thread Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-view-full-thread.png">
    </details>
    <br>
    <details><summary>Search Results Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-search-results.png">
    </details>
    <br>
    <details><summary>Manage Users Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-manage-users.png">
    </details>
    <br>
    <details><summary>Manage Contacts Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-manage-contacts.png">
    </details>
    <br>
    <details><summary>Edit User Profile Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-edit-user.png">
    </details>
    <br>
    <details><summary>Edit User - Admin Page</summary>
    <img src="beachhuts/static/docs/testing/ws-light-edit-user-admin.png">
    </details>
    <br>
    <details><summary>Generic Delete Modal</summary>
    <img src="beachhuts/static/docs/testing/ws-light-Delete-modal.png">
    </details>
    <br>

### Functional Testing

- #### Navigation Links

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design.

This was done by clicking on the navigation links on each page on a desktop, laptop, tablet and mobile device.

Additionally, Adminstrator and basic user accounts were created to check that correct menu options were presented and enhanced functionality restricted to Administrator privileged accounts. 

Modals and forms display as expected. Edit/Delete functions are correctly restricted to the appropritae owner and user account class. 'Cancel' buttons work as expected.

Links on all pages navigated to the correct pages as expeccted. External content opens in a new page.

-   #### Testing Approach



-   #### Test Accounts:
-   The folowing user accounts were created via the signup function rather than direct sql input to test the signup functionality:

    -   Admin:
        *   Username: admin@admin.bhas
        *   Password: 12345678    

    -   Normal Users:
        *   Username: userone@user.bhas
        *   Password: 12345678  

        *   Username: usertwo@user.bhas
        *   Password: 12345678 

        *   Username: noposts@user.bhas
        *   Password: 12345678 

        *   Username: nothing@user.bhas
        *   Password: 12345678 

-   #### Sign Up Testing
    -   The cursor is automatically positiioned at the start of the first input field.

    -   Accounts are created with a unique ID and posted to the database correctly. Each field is correctly validated and the account cannot be created until all fields are populated with the correct minimum and maximum values.

    -   Email address must be unique and the database is checked for duplicates. Password is checked to ensure it has been entered correctly.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

-   #### Log In Testing
    -   The cursor is automatically positiioned at the start of the first input field.

    -   Email address and password are validated against the database.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

-   #### Thread Post Testing
    -   The cursor is automatically positiioned at the start of the first input field.

    -   The user must be logged in for the 'Post' options to appear. Duplicate Post titles are permitted. Fields are validated for minimum character rules. Title and content body are mandatory fields.

    -   A maximum of 4 tags can be added. Attempting to add a fifth generates a suitable error. Tags are optional.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

    -   Successful submission generates a confirmation Flash message and creates a record on the Thread table linked to the correct User. This is tested by online enquiry and psql query in the cli.

    -   Users can edit and delete their own threads only and menus only appear if the logged in user has the correct permissions.

    -   Admin users can edit and delete all posts.

    #### Thread Enquiry Testing
    -   The Home page displays a list of posts(threads) together with the first comment (if any) with most recent presented first. If Logged in, Comment, Edit and Delete buttons are presented according to thread and comment owner and admin status. This was tested extensively with teh various test accounts.

    -   When Logged in the Home page also displays a summary of the User profile with a link to 'View My Posts'.
        -   This presents a list of all threads created by the current logged in user, together with all associated comments.
        -   If there are no Threads then comments owned by the current user are displayed.
        -   If there are neither threads nor posts then a suitable message is diaplayed with an invittaion to create a post.

    -   Where a thread contains multiple comments, a 'View Full Post' button is presented. This displays the Thead post and all associated comments.

    -   Signifiicant testing was carried out using the test logins to simulate all the above scenarios, specifically that correct permissions were being applied to thread and comment edit and delete functions.

    -   Edits were correctly applied to the database. Records were correctly deleted, including and associated records by cascade.

-   #### Comments Creation Testing

    -   The cursor is automatically positiioned at the start of the first input field.

    -   The user must be logged in for the 'Comment' option to appear. The comment body is validated for minimum character rules. Content body is a mandatory field.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

    -   Successful submission generates a confirmation Flash message and creates a record on the Comments table linked to the correct Thread and User. This is tested by online enquiry and psql query in the cli.

     -   Users can edit and delete their own comments only and menus only appear if the logged in user has the correct permissions.

    -   Admin users can edit and delete all comments.

    #### Comments Enquiry Testing

    -   The cursor is automatically positiioned at the start of the first input field.

    -   The user must be logged in for the 'Comment' option to appear. The comment body is validated for minimum character rules. Content body is a mandatory field.

    -   Errors are presented as a Flash message below the sub menu and hero image. 

    -   Successful submission generates a confirmation Flash message and creates a record on the Comments table linked to the correct Thread and User. This is tested by online enquiry and psql query in the cli.

     -   Users can edit and delete their own comments only and menus only appear if the logged in user has the correct permissions.

    -   Admin users can edit and delete all comments.

-   #### Tags Testing
 
    -   The Tags button directs to the 'Browse Tags' page where users can view existing category tags and add new ones.

    -   Only administrators can delete tags, so the option is hidden for ordinary users. 

    -   For Adding Tags:

        -   The cursor is automatically positiioned at the start of the first input field.
     
        -   Tag Case is forced to lowercase. Duplicate Tags are not permitted.

        -   Errors are presented as a Flash message below the sub menu and hero image. 

-   #### Manage Users Testing

    -   Accessible from the 'Users' button visible only to administrators.

    -   Once selected for Edit:

        -   The cursor is automatically positiioned at the start of the first input field.

        -   The form is pre-populated with existing database values.

        -   Changes to values are validated. The databse is only updated for values that have changed.

        -   Each field was updated in turn and also the form was submitted with no changes. Results were checked by online enquiry and via psql and were as anticipated.

        -   Admin status toggle was checked and worked as expected.

        -   Errors are presented as a Flash message below the sub menu and hero image. 

-   #### Manage Contacts Testing

    -   Accessible from the 'Contacts' button visible only to administrators.

    -   There is a separate entry for each contact message created. Field titles are minimised as this is an admin page so they really should be familiar with record layout.

    -   The only option is to 'Delete' which removes the record from the database. This was checked by online enquiry and psql query.

    -   Error and success Flash messages are presented below the sub menu and hero image. 

-   #### Search Function Testing

    -   It's possible to search on content within the tags, thread title and thread body content whether logged in or not. 

    -   This was tested with a variety of search terms and produced expected results.

    -   Searches for non existent content produces an empty search page. Searches are case insensitive.

-   #### Contact Testing

    -   Testing was performed to ensure that 

    -   The form on the contact page was tested to ensure it functioned as expected when correct and incorrect data was input.

    -   Specifically:

        -   Missing one or more input field: An error was highlighted to the user and the form could not be submitted.

        -   Incorrect email format: An error was highlighted to the user and the form could not be submitted.
    
        -   Form completed correctly with valid information in all fields: The form is able to be submitted.

        -   Form textarea will only accept a minimum of 1 and a maximum of 280 characters.

        -   Succesful submission of the contacts/feedback form: A confirmation Flash message is displayed. 

- ### Links Testing

Testing was performed to:

-   Open each hyperlink on each page and check that it is a valid URL and opens in a new page.

-   Checked on desktop, tablet and mobile.

-   ### Footer Social Media Icons / Links

Testing was performed on the Font Awesome Social Media icons in the footer to ensure that each one opened in a new tab and that each one
had a 'grow' hover effect.

Each item opened a new tab when clicked as expected and correct hover effect was present.

-   ### Footer Contact Information

The 'go to' link reacts when hovered over.

### Further Testing

-   Testing was carried out as each function was developed. The menu structure, navigation and footer were tested until error free on base.html before other page fucntionality was developed.
-   Code for creation, edit and delete was tested with Models that didnt update the database to check processing functionality before data chnages were attempted.
-   Admin and normal user accounts were created to support testing of restricted/enhanced permissions.
-   As each page was completed, existing succesful tests were rerun to ensure that proven functionality hadn't been affected. 
-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7/8/X and iPad.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.


### Bugs and Fixes

*   db_create would not work as advised on this version of python. I obtained the correct syntax from a web forum.

*   Model changes would not propogate to Heroku despite Databse recreation. This was solved by creating a new Sql hosting instance and updating Heroku config.

*   Permissions not being applie dto admin accounts caused by an errant 'div'.

*   Search bar woudlnt line up with icon. Margins and padding on standard bootstrap settings overwritten by css changes. 

*    Posts and commnets not consistently displaying. Moved formatting to earlier in loop processing.

*   Comment processing causing Model error. Confusion over singular comment (db field) and comments (table name).

*   Password Model length too small for hashed value. Increased to 255, db created and changes propogated to Heroku.

*   Manage user passing current user value through (admin) rather than user to be edited. Return value in Manage-user Model changed from current_user.

-   WCAG contrast issues.
    - Fixed - Minor colour scheme changes.

### Known Bugs

- There are no known errors.  

### Future Releases
-   Ideas for future development could include:
    -   Enabling pictures to be added to posts.
    -   User password self reset.

## Deployment

### Version Control

The site was created using the Visual Studio code editor and pushed to the remote repository on GitHub: ‘beach_hut_society’.

The following git commands were used throughout development to push code to the remote repository:

```git add <file>``` 
    - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”```
    - This command was used to commit changes to the local repository queue ready for the final step.

```git push origin main``` 
    - This command was used to push all committed code to the remote repository on github.

### Clone the Repository Code Locally

- Navigate to the GitHub Repository you want to clone to use locally:

    - Click on the code drop down button.
    - Click on HTTPS.
    - Copy the repository link to the clipboard.
    - Open your IDE of choice (git must be installed for the next steps).
    - Type git clone copied-git-url into the IDE terminal.

The project will now have been cloned on your local machine for use.

### Heroku

The project was deployed to Heroku using the following steps:

### App Deployment to Heroku

- You will need to deploy the application using Heroku.

1. Create a requirements.txt file:
    -   Type ``` pip3 freeze --local > requirements.txt ``` in theGitpod CLI.
    -   This shoudl be added to the .gitignore file.
2. Create a Procfile:
    -    Type ```echo web: python app.py > Procfile```.
    -    Open it and remove any spurious lines. It should have a singular line and commence with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - DATABASE_URL : This is the location of your production database.
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right:
  - Select run console.
  - Enter ```python3``` to access the python intepreter.
  - Enter:
    - ```From beachhut import app, db```
    - ```app.app-context().push()```
    - ```db.create_all()```
    - You can then exit the console with ```exit()```

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction):
    -   Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [jQuery:](https://jquery.com/): 
    -   jQuery is used to make the JavaScript code more succinct and simplify some processing.

### Content

-   All content was written by the developer with a great deal of assistance from youtube tutorials and stack overflow.

-   Mostly trial and error and getting one function working and then replicating it.

-   Inspiration was taken from existing blog sites and sample projects:
    -   https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy

### Media

-   Free background removal on various images using [photoroom](https://www.photoroom.com/tools/background-remover). 

-   The main background image is a standard Microsoft image. Other images are copyright free.

### Acknowledgements

-   My Mentor for his continuous helpful feedback and support. His industry experience is noticeable in his insighteful guidance. 

-   I can't overestimate the value of Stackoverflow resources at their website and on Youtube.

-   The whole community of developers who freely advise and share their knowledge via blogs, videos and web comments.

-   Tutor support at Code Institute for their support.

-   Tutor support at City of Bristol College for continued support and motivation.
