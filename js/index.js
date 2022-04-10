let map;
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 39.874, lng: 32.747 },
    zoom: 18,
  });
}

const marker = new google.maps.Marker({
  map,
  position: { lat: 39.874, lng: 32.747 },
});

if ("geolocation" in navigator) {
  navigator.geolocation.getCurrentPosition(
    (position) =>
      console.log(
        `Lat: ${position.coords.latitude} Lng: ${position.coords.longitude}`
      ),
    (err) => alert(`Error (${err.code}): ${err.message}`)
  );
} else {
  alert("Geolocation is not supported by your browser.");
}
//handle latitude and longitude inputs
const latInput = document.getElementById("latitude");
const lngInput = document.getElementById("longitude");

//listener for submitlocation
const submitLocation = document.getElementById("submitLocation");
submitLocation.addEventListener("click", (e) => {
  alert("Lat: " + latInput.value + " Lng: " + lngInput.value);
  e.preventDefault();
  //if latitude ang longitude are not float, alert an error message and return
  const lat = parseFloat(latInput.value);
  const lng = parseFloat(lngInput.value);

  if (!parseFloat(latInput.value) || !parseFloat(lngInput.value)) {
    alert("Please enter a valid latitude and longitude");
    return;
  }
  //if latitude and longitude are valid, set the marker position to the new location
  marker.setPosition({
    lat: lat,
    lng: lng,
  });
  //set the map center to the new location
  map.setCenter({
    lat: lat,
    lng: lng,
  });

  //calculate distance to the Geographic North Pole (Terrestrial North Pole)
  const distance = google.maps.geometry.spherical.computeDistanceBetween(
      marker.getPosition(),
      { lat: 90, lng: 0 }
    ),
    //convert distance to km
    distanceKm = distance / 1000,
    //convert distance to miles
    distanceMiles = distance / 1609.34;
  //display distance to the user
  document.getElementById(
    "distance"
  ).innerHTML = `Distance to the North Pole: ${distanceKm.toFixed(
    2
  )} km (${distanceMiles.toFixed(2)} miles)`;
});
