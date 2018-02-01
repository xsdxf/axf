$(function () {

    initSwiperWheel();
    initSwiperMustBuy();

})

function initSwiperWheel() {

    var swiper = new Swiper('#topSwiper',{
        autoplay:4000,
        pagination:'.swiper-pagination'
    })
}

function initSwiperMustBuy() {

    var swiper = new Swiper('#swiperMenu',{
        slidesPerView:3
    })
}