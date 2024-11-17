# My Beach Hut Appreciation Society Website

![Mockup](docs/readme_images/site_mockup.jpg)

**Author Neil Allen**

## Beach Hut Appreciation Society

This is my website   

[View the live project here.](https://beach-hut-appreciation-society-0c8700c133d2.herokuapp.com/)

# Table of Contents

1. [Project Inception and Planning](#project-inception-and-planning)
2. [User Experience (UX)](#user-experience-ux)
    *   [User stories](#user-stories)
        *   [First Time Visitor Goals](#first-time-visitor-goals)
        *   [Returning Visitor Goals](#returning-visitor-goals)
        *   [Frequent User Goals](#frequent-user-goals)
    *   [Design](#design)
        *   [Colour Scheme](#colour-scheme)
        *   [Typography](#typography)
        *   [Imagery](#imagery)
        *  [Design Considerations](#design-considerations)
    *   [Wireframes](#wireframes)
        *   [Index](#home)
        *   [Sign Up](#sign-up)
        *   [Log In](#log-in)
        *   [About](#about)
        *   [Contact](#contact)
        *   [Edit Profile](#edit-profile)
        *   [Edit Profile - Admin](#edit-profile---admin)
        *   [View All posts](#view-all-posts-for-user)
        *   [Posts](#posts)
            *   [Create Post](#create-a-new-post)
            *   [Edit Post](#edit-post)
            *   [Delete Post](#delete-post)
        *   [Comments](#comments)
            *   [Add Comment](#add-comment)
            *   [Edit Comment](#edit-comment)
            *   [Delete Comment](#delete-comment)
        *   [Tags](#tags)
            *   [Add Tag](#add-tag)
            *   [Delete Tag](#delete-tag)
        *   [Manage Users](#manage-users)
        *   [Search Results](#search-results)
        *   [404](#404)
    *   [Structure](#structure)
3. [Features](#features)
    *   [Landing Page](#landing-page)

    *   [Contact Page](#contact-page)

    *   [Error 404 Page](#error-404-page)
    *   [Site Features](#site-features)
4. [Technologies Used](#technologies-used)
    *   [Development Environment](#development-environment)
    *   [Languages Used](#languages-used)
    *   [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
5. [Testing](#testing)
    *   [HTML](#html)
    *   [CSS](#css)
    *   [JavaSceipt](#javascript)
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
        *   [Quiz Testing](#quiz-testing)
        *   [Form Testing](#form-testing)
        *   [Links Testing](#links-testing)
        *   [Footer Contact Information](#footer-contact-information)
    *   [Further Testing](#further-testing)
    *   [404 Error Testing](#404-error-testing)
    *   [Bugs and Fixes](#bugs-and-fixes)
    *   [Known Bugs](#known-bugs)
    *   [Future Releases](#future-releases)
6. [Deployment](#deployment)
    *   [Version control](#version-control)
    *   [Github Pages](#github-pages)
    *   [Deployments to Github Pages](#deployment-to-github-pages)
    *   [Clone the repository locally](#clone-the-repository-code-locally)
7. [Credits](#credits)
    *   [Code](#code)
    *   [Content](#content)
    *   [Media](#media)
    *   [Acknowledgements](#acknowledgements)

## Project Inception and Planning

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, .
        2. As a First Time Visitor, 
        3. As a First Time Visitor, 

    -   #### Returning Visitor Goals

        1. As a Returning Visitor,
        2. As a Returning Visitor, 
        3. As a Returning Visitor, 
    -   #### Frequent User Goals
        1. As a Frequent User, 
        2. As a Frequent User, 
        3. As a Frequent User, 

-   ### Design
    -   #### Colour Scheme
        -   I've used the pastel beach themed colours to reflect the subject matter of the site. A pale blue (#C8E4FD) background for the body.
        Titles alternatively in Dark Blue (#4203BF) and Sand (#DA5619) with text in Light Blue and Sand. Buttons are consistent according to function.
        -   General navigation buttons are similarly styled and edit, comment and delete buttons are styled differently to differentiate but remain consistnet amongst the forum post and tag elements.
        -   Some colours were muted or changed to meet WAVE guidelines during final stage testing. 
        
    -   #### Typography
        -   The fonts chosen are Original Surfer and Seaweed Script to adhere to teh beach theme. Seaweed Script is novel but unsuitable for use in large text blocks as it can make it difficult to read. Sans-serif is the fallback font.
 
    -   #### Imagery
        -   There is a Hero image in teh base template which propogates to each page and gives the site a consistenmt look and feel.
        -   There is a beach logo on larger screens but is hidden below 1000px.
        -   The site has a couple of additional images on the About page but as a blog site is mostly text based, for now..

    -   #### Design Considerations
        -   The site is built with templates based on Base.html so retains a consistent Header and Footer
     
        -   Colours are Bold yet soft and are selected to communicate a fun, beach theme and reflect the varied colours that are common to beach hut installations.

        -   The header and footer occupy the whole width of teh screen but contnet has wide margins on larger screen sizes with thin margins for tablet and mobile views.

        -   The site is responsive with menus and text resized for smaller screens. 

        -   Menu navigation is consistent across all pages and screen sizes and is central to each page. Menus change according to login and admin status.

        -   Menu button text is Sand witha  yellow background. The admin only function is highlighted in Green.

        -   There is a customised error-404 page 'just in case'.

        -   There are popup confirmations on all Delete functions and each update page also offers a 'cancel' function rather than expecting teh user to use tha back button or actively click elsewhere.

        -   Administrators have additional functions which are presented when they access different ares of the site.

        -   Error and confirmation messages are displayed at the top of the main site area, below the secondary menus. I chose not to make these disappear automatically or after a stated time as I personally find that inconvenient and prefer to have messages displayed until i have read that at my pace and taken action to dismiss them.
        
        -   Threads(posts) and the first comment are visible to all visitors but user have to register and login to see full posts or comment.

        -   Logged in users get to see their user profile, can edit it and can see all their own posts on a 'view all posts' page. I chose not to allow users to delete their own accounts as that would remove contnet from the site, incluidng any responses from other users. 

-   ### Wireframes

-   #### Base
    <details><summary>Base Template</summary>
    <img src="/workspace/beach_hut_society/beachhuts/static/docs/readme_images/screens/base-html.png">
    </details>

-   #### Home
    <details><summary>Home - Logged In</summary>
    <img src="/workspace/beach_hut_society/beachhuts/static/docs/readme_images/screens/home-logged-in.png">
    </details>
    <br>
    <details><summary>Home - Logged Out</summary>
    <img src="/workspace/beach_hut_society/beachhuts/static/docs/readme_images/screens/home-logged-out.png">
    </details>
    <br>

-   #### Sign Up
    <details><summary>Sign Up</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Log In
    <details><summary>Log In</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### About
    <details><summary>About</summary>
    <img src="/workspace/beach_hut_society/beachhuts/static/docs/readme_images/screens/about.png">
    </details>

-   #### Contact
    <details><summary>Contact</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/contact.png">
    </details>
    <br>

-   #### Edit Profile
    <details><summary>Edit profile</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Edit Profile - Admin
    <details><summary>Edit profile, Administrator</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### View All Posts For User
    <details><summary>View All posts For A User</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Posts
-   ##### Create A New Post
    <details><summary>Create A New Post</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/create-post.png">
    </details>

-   ##### Edit Post
    <details><summary>Edit post</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   ##### Delete Post
    <details><summary>Delete post</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Comments
-   ##### Add Comment
    <details><summary>Add Comment</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/add-comment.png">
    </details>

-   #### Edit Comment
    <details><summary>Edit Comment</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Delete Comment
    <details><summary>Delete Comment</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Tags
-   ##### Add tag
    <details><summary>Add Tag</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/tags.png">
    </details>

-   ##### Delete Tag
    <details><summary>Delete Tag</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Manage Users
    <details><summary>Manage Users</summary>
    <img src="/workspace/beach_hut_societybeachhuts/static/docs/readme_images/screens/.png">
    </details>

-   #### Search Results 
    <details><summary>Search Results</summary>
    <img src="docs/readme_images/404-desktop.png">
    </details>

-   #### 404 
    <details><summary>404 -Desktop</summary>
    <img src="docs/readme_images/404-desktop.png">
    </details>

 
-   ### **Structure**

    The structure of the site is informed by the the target audience's expectations and the principles of IXD (interaction design) to make sure I was making everything as intuitive as I could. Each page has a clear function and is named to give a clear indication of content/function.

    The site has a simple structure made up of 4 pages:
    * Homepage - An introduction 
    * 
    *
    * Comments - A form to allow the user to send comments or requests for further information.

    * There is one additional sub page and a confirmation popup on sucessful/failed email sending:
        -   A Confirmation thank you popup for when a user has successfully submitted a form and an email has been sent. Alternatively, a Confirmation thank you popup with a link to send a direct email if the form submission fails.
        -   A 404 page for when a user lands on a non-existent page.

    The site has a navbar which remains central to the screen on desktop, tablet and mobile, this allows a user to access any page they need at any time and is suitable for a first time or returning visitor. The active button is a different shape to distinguish it. There is also a footer on every page with links to social media sites and the Comments page.

    Each page logo, except the Home Page itself, has a link back to Home. Each page has a scrolling 'top of page' anchor link.

    Social media links all point to the
    
## Features

-   Responsive on all device sizes down to 280px - the industry standard minimum screen width.

-   Home page 

-   

-   Inactive menu pages are 
-   
    <details><summary>Navigation Menu</summary>
    <img src="docs/readme_images/navbar.jpg">
    </details>
    <br>
-   Each page also has a floating anchor link at the side to take the user back to the top of the page. Some pages also have links directly to myth or quiz pages or both.
    <details><summary>Bottom links</summary>
    <img src="docs/readme_images/page_links.jpg">
    </details>
    <br>
    <details><summary>Anchor link to Top</summary>
    <img src="docs/readme_images/anchor_top_link.jpg">
    </details>
    <br>
-  Scrolling text box with help text on comments page.
    <details><summary>Comments Text Box</summary>
    <img src="docs/readme_images/comments.jpg">
    </details>
    <br>

### Landing Page
* Landing page image
    * This is an in
    * This will help to immediately show the user what the website is about. 
    <br>
    <details><summary>Landing Page</summary>
    <img src="docs/readme_images/landing_page.jpg">
    </details>
    <br>

* Expanding buttons.
    * Additional information is 
    * This information lets the user know what the site is.
    <br>
     <details><summary>Homepage Details</summary>
    <img src="docs/readme_images/landing_page_detail.jpg">
    </details>
    <br>

### Page
* 
    * 
    <br>  
    <details><summary>Myth Page</summary>
    <img src="docs/readme_images/myth_page.jpg">
    </details>
    <br>
    <details><summary>Myths - front of card</summary>
    <img src="docs/readme_images/myth_details_page.jpg">
    </details>
    <br>
    <details><summary>Myths - rear of card</summary>
    <img src="docs/readme_images/myth_details_page2.jpg">
    </details>


###  Page
* 
    *  
    <br>
    <details><summary>Quiz Page</summary>
    <img src="docs/readme_images/quiz_page.jpg">
    </details>
    <br>    
    <details><summary>Quiz Page Details</summary>
    <img src="docs/readme_images/quiz_details_page.jpg">
    </details>

### Contact Page
* Contact form
    * A contact is offered to allow users to contact me. The form consists of the following fields and attributes: 
        * First Name (required, type=text).
        * Last Name (required, type=text).
        * Email (required, type=email).
        * Message (required, type=textarea), maximum 280 characters.
    * Muted Text is used as hints or for assurance on certain fields. This has been adjusted for WCAG compliance.
    * This allows a user to contact me if they have any queries about Autism or wish to give any feedback on the site.
    * A popup modal confirms when a successful email has been sent using the emailJS service and gmail.
    * If the message send fails then an alternative popup message is displayed.
    <br>
    <details><summary>Contact Page</summary>
    <img src="docs/readme_images/Screenshot_contact_info_page.jpg">
    </details>

### Confirmation Popup
* On successful submission of the contact form, the user will be presented with a popup displaying a success message.

* This can be dismissed by clicking on the "close" button, clicking outside of the message box or clicking on the Autism Awareness logo on the message.

    <details><summary>Contact Confirmation Popup</summary>
    <img src="docs/readme_images/Screenshot_Contact_confirmation.jpg">
    </details>

* If the form submission is unsuccessfuli, the user will be presented with a popup displaying a failure message.

* This can be dismissed by clicking on the "close" button, clicking outside of the message box or clicking on the Broken Autism Rainbow Heart logo logo on the message.

    <details><summary>Contact error/failed Popup</summary>
    <img src="docs/readme_images/Screenshot_Contact_confirmation_fail.jpg">
    </details>

### Error 404 Page
* Error 404 Page
    * There is a bespoke 404 error page to trap any file not found errors. This enables the user to access the menu structure in the event of a missing page or file and avoids use of the 'back' button were a default 404 page displayed.
    
    * The usual menu navbar will be present on this screen. There is no requirement for a footer.

    <details><summary>Error 404</summary>
    <img src="docs/readme_images/Screenshot_error_404.jpg">
    </details>

### Site Features

* Responsive design - content scales from 280px to Large Desktop. Some content is hidden at smaller resolutions to maintain user experience.
* Menu navbar remains consistent with a 
* There is a Top of the Page scrolling button on each page. 
* The main landing page contains information about 
* Contact form and success/fail confirmation pages.
* There are links to other social media and resources.
* The site is clean and uncluttered and follows a Beach theme.
* Bespoke 404 page with navbar.

## Technologies Used

### Development Environment
-   The site was developed in a [Gitpod](https://www.gitpod.io/) environment using VSC.

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   pytho


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.2.1:](https://getbootstrap.com/docs/4.2/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Menu items in the navbar as well as the Social Media icons in the footer to add the 'grow' transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Baskerville Libre' and 'Open Sans' fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Used for icons on social links and drop down menus.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to make the navbar responsive and provide additional coding flexibility. specifically used with the emailJS service, modal and other processing.
1. [Gitpod](https://www.gitpod.io/)
    - GitPod was used for version control by utilizing the GitPod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from the development environment.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](#wireframes) during the design process.
1. flask

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the website to ensure there were no syntax errors in the project.

### HTML

This was carried out periodically as each page was created and amended and then finally checked again when pages were deemed complete and error free.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)

    <details><summary>Home Page</summary>
    <img src="docs/testing/w3-index-check.jpg">
    </details>
    <br>
    <details><summary>Myths Page</summary>
    <img src="docs/testing/w3-myths-check.jpg">
    </details>
    <br>
    <details><summary>Quiz Page</summary>
    <img src="docs/testing/w3-quiz-check.jpg">
    </details>
    <br>
    <details><summary>Contact Page</summary>
    <img src="docs/testing/w3-contact-check.jpg">
    </details>
    -   Confirmation/failure modal code is in contact.html so was checked by scanning contact page.
    <br>
    <br>
    <details><summary>Error 404 Page</summary>
    <img src="docs/testing/w3-404-check.jpg">
    </details>

### CSS

This was checked periodically as each page was created and CSS code added and amended. A final check was carried out when all other testing had been satisfactorily completed.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

    <details><summary>style.css</summary>
    <img src="docs/testing/ws-style-css-check.jpg">
    </details>
    <br>

### JavaScript

This was checked periodically as each page was created and CSS code added and amended. A final check was carried out when all other testing had been satisfactorily completed.

-   [jshint JavaScript Validator](https://jshint.com/)

    <details><summary>Main JS - scripts.js</summary>
    <img src="docs/testing/jshint-scripts-js.jpg">
    </details>
    <br> 
    <details><summary>Email specifc js -cemail.js</summary>
    <img src="docs/testing/jshint-email-js.jpg">
    </details>
    <br> 
    <details><summary>Quiz qQuestion arrays - quiz.js</summary>
    <img src="docs/testing/jshint-quiz-js.jpg">
    </details>
    <br>    

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    
    1. As a First Time Visitor,
        
        1. 
        2. 

    2. As a First Time Visitor, 

        1. 
        2. 
        3.

    3. As a First Time Visitor,
       
        1. 
        2. 
        3. 
-   #### Returning Visitor Goals

    1. As a Returning Visitor,
       
        1. . 
        2. 
        3. 

    3. As a Returning Visitor, 

        1. Each page footer has a clear link to the comments and feedback page to send a message.
        2. Each page menu bar has a link to the comments and feedback page where a user can submit a request for more information.

    4. As a Returning Visitor,
       
        1. 

-   #### Frequent User Goals

    1. As a Frequent User,
        
        1. 
        2. 

    3. As a Frequent User,
        
        1. 
        2. 

    5. As a Frequent User, 

        1. 
        2. 
        
### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 280px and upwards as defined in [WCAG 2.1 Reflow criteria for responsive design](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html) on the following browsers:
- Chrome    (123.0.6312.106).
- Edge      (123.0.2420.81).
- Firefox   (124.0.2).
- Safari    (17.4).
- Opera     (109.0.5097.24).

Steps to test:

1. Open browser and navigate to
[vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv).
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

<details><summary>Home Page</summary>
<img src="docs/testing/wave-index.jpg">
</details>
<br>
-   Warnings on some pages report that "Adjacent links go to the same URL." This is because the link to home page(menu) is close to the link to home page(title icon).
<br>
<details><summary>Page</summary>
<img src="docs/testing/wave-myth.jpg">
</details>
<br>
<details><summary> Page</summary>
<img src="docs/testing/wave-quiz.jpg">
</details>
<br>
-   contact success/fail screen content part of contact page.
<details><summary>Contact Page</summary>
<img src="docs/testing/wave-contact.jpg">
</details>
<br>
<details><summary>Error 404 Page</summary>
<img src="docs/testing/wave-404.jpg">
</details>
<br>

Manual tests were also performed to ensure the website was as accessible as possible.

### Screen Reader

Screen reader testing was performed using NVDA software from [NV Access](https://www.nvaccess.org/).
This confirmed that:

-   All text is readable.
-   All images have accurate, useful text descriptions.

### Lighthouse Testing

<details><summary>Home Page</summary>
<img src="docs/testing/lighthouse_home_page.jpg">
</details>
<br> 
<details><summary> Page</summary>
<img src="docs/testing/lighthouse__page.jpg">
</details>
<br>
<details><summary> Page</summary>
<img src="docs/testing/lighthouse__page.jpg">
</details>
<br>
<details><summary>Contact Page</summary>
<img src="docs/testing/lighthouse_contact_page.jpg">
</details>
<br>
<details><summary>Error 404 Page</summary>
<img src="docs/testing/lighthouse_404_page.jpg">
</details>

### Functional Testing

- ### Navigation Links

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design.
This was done by clicking on the navigation links on each page on a desktop, laptop, tablet and mobile device.

Links on all pages navigated to the correct pages as expeccted. External content opens in a new page.

-   ###  Testing
Testing was performed to ensure that 

The form on the contact page was tested to ensure it functioned as expected when correct and incorrect data was input.

Specifically:

-   Missing one or more input field:
    An error was highlighted to the user and the form could not be submitted.

-   Incorrect email format:
    An error was highlighted to the user and the form could not be submitted.
    
-   Form completed correctly with valid information in all fields:
    The form is able to be submitted.

-   Form textarea will only accept a minimum of 1 and a maximum of 280 characters.

-   Succesful submission of the contacts/feedback form: A confirmation message is displayed. 

-   Incorrect submission was emulated by temporarily amending emailJS validation information to force an error. The "failed" confirmation message was displayed as expected and could be dismissed. 

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

-   Testing was carried out as each function was developed. The menu structure, navigation and footer were tested until error free on index.html before propogating to other pages.
-   As each page was completed, existing succesful tests were rerun to ensure that proven functionality hadn't been affected. 
-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7/8/X and iPad.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Contact email Testing
-  A series of contact forms were successfully completed and emails sent. Emails were received into the webdev1961 gmail account:

-   The confirmation message is presented and disappears when clicked.
-   A forced error on emailJS produces the 'failed to send' message. It's possible to either close this or send a direct email from the link.

<details><summary>Webdev Email</summary>
<img src="docs/testing/contact_email.jpg">
</details>
 
###

###

###

### 404 Error Testing

-   A bespoke 404 error page has been created to provide a better user experience.
-   This was tested by:
    - Navigating to the contact page and changing the address to contact404.html in the browser.
    - The dedicated 404-error was displayed and it was possible to navigate home via the home button.

### Bugs and Fixes

-   

-   WCAG contrast issues.
    - Fixed - Minor colour scheme changes.

### Known Bugs

- There are no known errors.  

### Future Releases
-   Ideas for future development could include:
    -   

## Deployment

### Version Control

The site was created using the Visual Studio code editor and pushed to the remote repository on GitHub: ‘beach_hut_society’.

The following git commands were used throughout development to push code to the remote repository:

```git add <file>``` 
    - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”```
    - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` 
    - This command was used to push all committed code to the remote repository on github.

### GitHub Pages

The project was deployed to GitHub Pages using the following steps:

### Deployment to Github Pages

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
    - In the GitHub repository, navigate to the Settings tab. 
    - From the menu on left select 'Pages'.
    - From the source section drop-down menu, select the Branch: main.
    - Click 'Save'.
    - A live link will be displayed in a green banner when published successfully. 

    [The live link can be found here](https://beach-hut-appreciation-society-0c8700c133d2.herokuapp.com/)


### Clone the Repository Code Locally

- Navigate to the GitHub Repository you want to clone to use locally:

    - Click on the code drop down button.
    - Click on HTTPS.
    - Copy the repository link to the clipboard.
    - Open your IDE of choice (git must be installed for the next steps).
    - Type git clone copied-git-url into the IDE terminal.

The project will now have been cloned on your local machine for use.

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

. [jQuery:](https://jquery.com/):
    - jQuery is used to make the JavaScript code more succinct and simplify some processing.

### Content

-   All content was written by the developer with some assistance from youtube tutorials and stack overflow.

### Media

-   Free background removal on various images using [photoroom](https://www.photoroom.com/tools/background-remover). 

-   Images were resized using [imageresizer](https://imageresizer.com/).

### Acknowledgements

-   

-   My Mentor for continuous helpful feedback and support.

-   Stackoverflow resources at their website and on Youtube.

-   The whole community of developers who freely advise and share their knowledge via blogs, videos and web comments.

-   Tutor support at Code Institute for his support.
