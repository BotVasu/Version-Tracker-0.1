const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
// const gitlogo = document.querySelector(".cta");


hamburger.addEventListener("click", () =>{

    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
    // gitlogo.classList.toggle("active");
})