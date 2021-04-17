document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');

  modeSwitch.addEventListener('click', function () {                     
      document.documentElement.classList.toggle('dark');
      modeSwitch.classList.toggle('active');
  });
  
  var listView = document.querySelector('.list-view');
  var gridView = document.querySelector('.grid-view');
  var projectsList = document.querySelector('.project-boxes');
  
  listView.addEventListener('click', function () {
    gridView.classList.remove('active');
    listView.classList.add('active');
    projectsList.classList.remove('jsGridView');
    projectsList.classList.add('jsListView');
  });
  
  gridView.addEventListener('click', function () {
    gridView.classList.add('active');
    listView.classList.remove('active');
    projectsList.classList.remove('jsListView');
    projectsList.classList.add('jsGridView');
  });
  
  document.querySelector('.messages-btn').addEventListener('click', function () {
    document.querySelector('.messages-section').classList.add('show');
  });

  /*Показ модального окна*/
  $('.add-btn').on('click',
          function () {
              $('.overlay,.modal').show();
          }
  );
  /*Закрытие модального окна*/
  $('.submit-button,.overlay,.close').on('click',function(){
      $('.overlay,.modal').hide();
  });

  $('input[type="file"]').change(function(){      
    var fileName = $(this).val().split('/').pop().split('\\').pop();
    // console.log(fileName);
    $('.input-file-name-info').text(fileName);
  });

  $('.card-3-button').on('click',
    function () {
      $('.overlay,.card-info').show();
    }
  );

  $('.overlay,.close').on('click',function(){
    $('.overlay,.card-info').hide();
  });

  $('.submit-button').on('click', () => {
    let form = {
      name: $('.task-name-input').val(),
      description: $('.task-description-input-field').val(),
      num_of_people: parseInt($('.people-num-input').val(), 10),
      file_ref: $('.file-ref-input').val()
    };


    console.log(form);

    fetch('/api/add/', {
      method: 'post',
      body: JSON.stringify(form)
    });
  });

});

fetch('/api/5/')
.then((response) => {
  if (response.status !== 200) {
    console.log("Ничего. Status: " + response.status);
    return;
  }

  response.json().then((data) => {
    console.log(data);

    let perc = 70;

    $('.card-3-date').text(data.date);
    $('.card-3-name').text(data.name);
    $('.task-name').text(data.name);
    $('.task-description').html(data.description.replace(/\n/g, "<br />"));
    $('.card-3-progress').text(perc + '%');
    $('.card-3-box-progress').css("width", perc + '%');
  });
})
.catch((error) => {
  console.log("Fetch error: -S", error);
});
