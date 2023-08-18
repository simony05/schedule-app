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
  fetch(`/activities/${time}`)
  .then(response => response.json())
  .then(activities => {
    
    // Loop through activities occurring in that time period, create <div> for each
    activities.forEach(activity => {
      console.log("hi")
      // Create div for each activity
      const new_activity = document.createElement('div');
      new_activity.innerHTML = `<h5>${activity.title}</h5>`;
      document.body.append(new_activity);
    })
  })
}
