document.addEventListener('DOMContentLoaded', function() {

  // Buttons go to respective views
  document.querySelector('#today').addEventListener('click', () => load_schedule('today'));
  document.querySelector('#week').addEventListener('click', () => load_schedule('week'));
  document.querySelector('#month').addEventListener('click', () => load_schedule('month'));

  // Load today by default
  load_schedule('today');
});

function load_schedule(time) {
if (time == "today") {
  document.querySelector('#today-view').style.display = 'block';
  document.querySelector('#week-view').style.display = 'none';
  document.querySelector('#month-view').style.display = 'none';
}
else if (time == "week") {
  document.querySelector('#today-view').style.display = 'none';
  document.querySelector('#week-view').style.display = 'block';
  document.querySelector('#month-view').style.display = 'none';
}
else {
  document.querySelector('#today-view').style.display = 'none';
  document.querySelector('#week-view').style.display = 'none';
  document.querySelector('#month-view').style.display = 'block';
}

fetch(`/activities/${time}`)
  .then(response => response.json())
  .then(activities => {
    console.log("hia")
    
    document.querySelector(`#${time}-view`).innerHTML = ""

    // Loop through activities occurring in that time period, create <div> for each
    
    activities.forEach(activity => {
      console.log("hi")
      // Create div for each activity
      document.querySelector(`#${time}-view`).innerHTML += `<h4>${activity.title}</h4>`
    })
  })
}
