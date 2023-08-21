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
    activities.forEach(activity => {
    console.log(activities)
    const button = document.createElement('button');
      button.innerHTML = "Delete";
      document.querySelector(`#${time}-view`).innerHTML += 
      `
      <div class="activity">
        <h4>${activity.title}</h4>
        <h5>${activity.content}</h5>
        <button id="delete_activity">Click</button>
      </div>
      `
      document.getElementById('delete_activity').addEventListener('click', delete_activity(activity.id, time))
    })
  })
}


function delete_activity(id, time) {
  fetch(`/delete_activity/${id}`)
  load_schedule(time);
}
