$(document).ready(function() {
    $('.container_1').css("display", "none");
    $('.container_2').css("display", "none");
    $('.container_3').css("display", "none");

    var lenPage = 400;
    var marPage = 200;
    var nContainers = 3;
            
    $(window).scroll(function() {
        //$('.main_img_container').css("height", $(window).height());
        //$('.main_str_container').css("height", $(window).height());
        //$('.container_1').css("height", $(window).height());
        var nPage = parseInt($(window).scrollTop() / (lenPage+marPage));
        console.log("Page=", nPage);
        switch (nPage){
            case 0:
                for(i = 1;i <= nContainers;i++)
                    $(`.container_${i}`).css("display", "none");
                
                if($(window).scrollTop() <= lenPage){
                    $('.main_img').css("opacity", 1 - $(window).scrollTop() / lenPage);
                    $('.main_str_container').css("opacity", $(window).scrollTop() / lenPage);
                    $('.main_str').css("font-size", `${($(window).scrollTop() / 100)}vw`);
                }else{
                    $('.main_img').css("opacity", 0);
                    $('.main_str_container').css("opacity", 1);
                }
                break;
            
            case 1:
                $('.container_1').css("display", "flex");

                if(($(window).scrollTop() - (marPage+lenPage)) <= lenPage){
                    $('.main_str_container').css("opacity", 1 - ($(window).scrollTop() - lenPage - marPage) / lenPage);
                    $('.container_1').css("opacity", ($(window).scrollTop() - lenPage - marPage) / lenPage);
                }else{
                    $('.main_str_container').css("opacity", 0);
                    $('.container_1').css("opacity", 1);
                }

            default:
                for(i = 1;i <= nContainers;i++)
                    if(i === (nPage-1) || i === nPage)
                        $(`.container_${i}`).css("display", "flex");
                    else
                        $(`.container_${i}`).css("display", "none");

                if(($(window).scrollTop() - (nPage * (marPage+lenPage))) <= lenPage){
                    $(`.container_${nPage-1}`).css("opacity", 1 - ($(window).scrollTop() - (lenPage + marPage)*nPage) / lenPage);
                    $(`.container_${nPage}`).css("opacity", ($(window).scrollTop() - (lenPage + marPage)*nPage) / lenPage);
                }else{
                    $(`.container_${nPage-1}`).css("opacity", 0);
                    $(`.container_${nPage}`).css("opacity", 1);
                }
                console.log((($(window).scrollTop() - marPage*nPage) % lenPage) / lenPage);
        }    
    });
});

function chart(){
    $('html,body').animate({scrollTop:1000}, 'fast');
}
