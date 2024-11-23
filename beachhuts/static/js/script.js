/* jshint esversion: 6 */
/*globals $:false */
  
// Scrolling side button - Get the button:
  let mybutton = document.getElementById("myHomeBtn");
    window.onscroll = function () {
    scrollFunction();
  }; // When the user scrolls down 20px from the top of the document, show the button
  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  
// When the user clicks on the button, scroll to the top of the document
  $("#myHomeBtn").click(function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  });

// Toggle the comments reply form and sets cursor at start of text area
  function showCommentForm(threadId) {
    let commentForms = document.querySelectorAll('.commentForm');
    commentForms.forEach(function(form) {
      if (form.getAttribute('data-thread-id') === threadId) {
          form.classList.remove('d-none');
          form.classList.add('d-block');
        }{
          $('#commentBody').focus();
          // https://www.sitepoint.com/jqueryhtml5-input-focus-cursor-positions/#:~:
          // text=To%20set%20the%20cursor%20position%20at%20the%20end%20of%20an,to%20set%20the%20cursor%20position.
        }
    });
  }

  function hideCommentForm(threadId) {
    let commentForms = document.querySelectorAll('.commentForm');
    commentForms.forEach(function(form) {
      if (form.getAttribute('data-thread-id') === threadId) {
          form.classList.remove('d-block');
          form.classList.add('d-none');
        }
    });
  }

// select 2 for multiselect - select2.org/getting-started/basic-usage
// Initialize select2

  $(document).ready(function () {
    $('#thread_tags').select2({
      placeholder: "Select Tags",
      tags: true,
      tokenSeparators: [',', ' '],
      // apply selection limit with Select2 (https://select2.org/selections)
      maximumSelectionLength: 4,
    });
  });