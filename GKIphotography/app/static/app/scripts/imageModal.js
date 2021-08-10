

// get elements
var images = document.querySelectorAll('.myImg');
var modalImage = document.querySelector('.modalImage');
var modal = document.querySelector('.bodyModal');
var modalCaption = document.querySelector('.bodyModal p');


function modalPopup(url, caption)
{

    // Write omage url to image container
    modalImage.src = url;


    //add open class to show modal popup
    modal.classList.add('open');
    modalImage.classList.add('open');
    modalCaption.innerHTML = caption;

    console.log(url)

}

modal.addEventListener('click', (e) => {
    if (e.target.classList.contains('bodyModal')) {
        modal.classList.remove('open');
        modalImage.classList.add('open');
    }
});
/*<div class="bodyModal">
    <img class="modalImage" src="../../static/app/Assets/camera-820018_1920.jpg" />
    <p>Caption test<p>
    </div>*/