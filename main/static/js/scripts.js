let input = document.querySelector('input')
let button = document.getElementById('submit_button')
let loader = document.getElementById('loader')
let status = document.getElementById('status')

input.addEventListener('change', updateValue)

function updateValue(e) {
  button.disabled = (e.target.value === '')
  status.hidden = true
}

button.addEventListener("click", onButtonTap)

function onButtonTap(e) {
  changeState(true)

  $.ajax({
    url: '/main/send_text/',
    data: {
      'text': input.value
    },
    dataType: 'json',
    success: function (data) {
      changeState(false)
      status.hidden = false
      status.innerText = data['is_disaster'] ? 'Disaster' : 'Not Disaster'
      status.style.color =data['is_disaster'] ? '#A52A2A' : '#5F9EA0'
    }
  });
}

function changeState(isLoading) {
  input.disabled = isLoading
  button.disabled = !isLoading
  loader.hidden = !isLoading
}

