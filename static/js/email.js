/*jshint esversion: 6 */
/*globals $:false */

function sendMail(contactForm) {
    emailjs.send("service_uajjbzw", "template_75wup1h", {
            "first_name": contactForm.firstname.value,
            "last_name": contactForm.lastname.value,
            "from_email": contactForm.emailaddress.value,
            "contact_form_message": contactForm.feedbackmessage.value
        })
        .then(
            // confirmation to user via modal
            //  reset form data in native JS
            function emailsent() {
                document.getElementById('contactForm').reset();
                $("#success-modal").modal('show');
            },
            // else log an error
            function (error) {
                document.getElementById('contactForm').reset();
                console.log("FAILED", error);
                $("#failure-modal").modal('show');
            }
        );
    return false; // To block from loading a new page
}

// close by Modal ID
$("#success").click(function () {
    $("#success-modal").modal('hide');
});

$("#failure").click(function () {
    $("#failure-modal").modal('hide');
});