document.addEventListener('DOMContentLoaded', function() {

    // Buttons go to respective views
    document.querySelector('#today').addEventListener('click', () => load_schedule('today'));
    document.querySelector('#week').addEventListener('click', () => load_schedule('week'));
    document.querySelector('#month').addEventListener('click', () => load_schedule('month'));

    // Load today by default
    load_schedule('today');
  });

function load_schedule(time) {
  document.querySelector('#schedule-view').innerHTML = "hi";
  if (time == "week") {
    document.querySelector('#schedule-view').innerHTML = "bye";
  }
  fetch('/activities/')
  .then(response => response.json())
  .then(activities => {
    
    // Loop through emails, create <div> for each
    activities.forEach(activity => {
      // Create div for each email
      const newActivity = document.createElement('div');
      newActivity.className = "list-group-item";
      newActivity.className = "border-style";
    })
  })
}

datepicker.min = new Date().toLocaleDateString('fr-ca');