// ==========================================
// Floating Contact Menu
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    const floatingContact = document.getElementById("floatingContact");
    const contactToggle = document.getElementById("contactToggle");

    if (floatingContact && contactToggle) {

        contactToggle.addEventListener("click", function (e) {

            e.stopPropagation();

            floatingContact.classList.toggle("active");
            contactToggle.classList.toggle("active");

        });

        document.addEventListener("click", function (e) {

            if (!floatingContact.contains(e.target)) {

                floatingContact.classList.remove("active");
                contactToggle.classList.remove("active");

            }

        });

        document.addEventListener("keydown", function (e) {

            if (e.key === "Escape") {

                floatingContact.classList.remove("active");
                contactToggle.classList.remove("active");

            }

        });

    }

});
/*==============================
      HERO COUNTER
==============================*/

const counters = document.querySelectorAll(".counter");

const runCounter = () => {

    counters.forEach(counter => {

        const target = +counter.dataset.target;

        let count = 0;

        const speed = target / 80;

        const update = () => {

            if(count < target){

                count += speed;

                counter.innerText = Math.ceil(count);

                requestAnimationFrame(update);

            }else{

                counter.innerText = target + "+";

            }

        }

        update();

    });

}

window.addEventListener("load", runCounter);
const navbar = document.querySelector(".custom-navbar");

window.addEventListener("scroll", () => {
    if (window.scrollY > 40) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});