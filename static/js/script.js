/*=========================================
        MEGA WALL - SCRIPT.JS
=========================================*/

document.addEventListener("DOMContentLoaded", () => {

    /*=========================================
            AOS
    =========================================*/

    if (typeof AOS !== "undefined") {

        AOS.init({
            duration: 900,
            once: true,
            offset: 80
        });

    }

    /*=========================================
            NAVBAR SCROLL
    =========================================*/

    const navbar = document.querySelector(".custom-navbar");

    const navbarScroll = () => {

        if (!navbar) return;

        if (window.scrollY > 40) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    };

    navbarScroll();

    window.addEventListener("scroll", navbarScroll);

    /*=========================================
            SMOOTH SCROLL
    =========================================*/

    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth",
                block: "start"

            });

        });

    });

    /*=========================================
        MOBILE NAVBAR AUTO CLOSE
    =========================================*/

    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navLinks.forEach(link => {

        link.addEventListener("click", () => {

            if (navbarCollapse.classList.contains("show")) {

                bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();

            }

        });

    });

    /*=========================================
            ACTIVE MENU
    =========================================*/

    const sections = document.querySelectorAll("section[id]");

    const activateMenu = () => {

        let current = "";

        sections.forEach(section => {

            const top = section.offsetTop - 120;

            if (window.scrollY >= top) {

                current = section.getAttribute("id");

            }

        });

        document.querySelectorAll(".navbar-nav .nav-link").forEach(link => {

            link.classList.remove("active");

            if (link.getAttribute("href") === "#" + current) {

                link.classList.add("active");

            }

        });

    };

    activateMenu();

    window.addEventListener("scroll", activateMenu);

    /*=========================================
            HERO COUNTER
    =========================================*/

    document.querySelectorAll(".counter").forEach(counter => {

        const target = Number(counter.dataset.target);

        if (!target) return;

        let current = 0;

        const step = Math.max(1, target / 80);

        const update = () => {

            current += step;

            if (current < target) {

                counter.textContent = Math.ceil(current);

                requestAnimationFrame(update);

            } else {

                counter.textContent = target + "+";

            }

        };

        update();

    });

       /*=========================================
            FLOATING CONTACT
    =========================================*/

    const floating = document.getElementById("floatingContact");
    const toggle = document.getElementById("contactToggle");

    if (floating && toggle) {

        // Boshlanishida menyu yopiq bo'ladi
        floating.classList.remove("active");

        // Chat tugmasini bosganda ochish/yopish
        toggle.addEventListener("click", function (e) {

            e.stopPropagation();

            floating.classList.toggle("active");

        });

        // Popup ichini bosganda yopilmasin
        const menu = floating.querySelector(".contact-menu");

        if (menu) {

            menu.addEventListener("click", function (e) {

                e.stopPropagation();

            });

        }

        // Tashqariga bosilganda yopiladi
        document.addEventListener("click", function () {

            floating.classList.remove("active");

        });

        // ESC bosilganda yopiladi
        document.addEventListener("keydown", function (e) {

            if (e.key === "Escape") {

                floating.classList.remove("active");

            }

        });

    }

    /*=========================================
            SCROLL TOP
    =========================================*/

    const scrollTop = document.querySelector(".scroll-top");

    if (scrollTop) {

        window.addEventListener("scroll", () => {

            if (window.scrollY > 500) {

                scrollTop.classList.add("show");

            } else {

                scrollTop.classList.remove("show");

            }

        });

        scrollTop.addEventListener("click", e => {

            e.preventDefault();

            window.scrollTo({

                top: 0,

                behavior: "smooth"

            });

        });

    }

});
