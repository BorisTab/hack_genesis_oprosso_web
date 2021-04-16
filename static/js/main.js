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
    $('.overlay,.close').on('click',function(){
        $('.overlay,.modal').hide();
    });

    $('input[type="file"]').change(function(){      
      var fileName = $(this).val().split('/').pop().split('\\').pop();
      // console.log(fileName);
      $('.input-file-name-info').text(fileName);

    });
  });