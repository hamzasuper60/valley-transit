limoAccess = []
$.get('/api/limo/list', function(data) {
    limoAccess = data
})


function loadPage() {
    const path = window.location.pathname;
    $.get(`/api/router?path=${path}`, function(data) {
        $('main').html(data)  
    })
}

function limoValidation() {
    const username = $('#robloxUsername').val()
    if (limoAccess.includes(username)) {
        $('#limoOption1').addClass('opacity-100').removeClass('opacity-0')
    } else {
        $('#limoOption1').removeClass('opacity-100').addClass('opacity-0')
        $('#limoOption2').removeClass('opacity-100').addClass('opacity-0')
    }
}

function destinationValidation() {
    const service = $('#service').val()
    if (service == "limo") {
        $('#limoOption2').addClass('opacity-100').removeClass('opacity-0')
    } else {
        $('#limoOption2').removeClass('opacity-100').addClass('opacity-0')
    }
}

function orderTaxi() {
    const robloxUsername = $('#robloxUsername').val()
    const characterName = $('#characterName').val()
    const location = $('#location').val()
    let service = $('#service').val()
    let destination = $('#destination').val()
    if (robloxUsername === "") return
    if (characterName === "") return
    if (location === "") return
    if (!limoAccess.includes(robloxUsername)) service = "taxi"
    if (!limoAccess.includes(robloxUsername)) destination = ""
    $.post(`/api/taxi/order`, {"robloxUsername": robloxUsername, "characterName": characterName, "location": location, "service": service, "destination": destination}, function(data) {
        $('#orderButton').addClass('opacity-0')
        setTimeout(function(){
            $('#orderButton').text('Order Sent!').attr('onclick', '').attr('disabled', 'true')
            $('#orderButton').removeClass('opacity-0')
        }, 150)
    })
}

function loadBusStops() {
    $.getJSON(`/api/bus/stops`, function(data) {
        data.forEach(element => {
            routes_html = ""
            element.routes.forEach(element => {
                routes_html = routes_html + `<span class="bg-green-600 text-white px-2 py-1 mr-1 rounded shadow">${element}</span>`
            })
            console.log('delata')
            $('#busStops').append(`
            <a class="border p-2 flex flex-wrap rounded shadow hover:bg-neutral-900 transition-all" href="/bus/times?stop=${element.id}">
                <div class="flex items-center justify-center flex-grow-0 p-2">
                    <i class="fa-solid fa-location-dot text-5xl"></i>
                </div>
                <div class="flex-grow ml-2">
                    <p class="text-xl font-semibold">${element.name}</p>
                    <p class="italic text-sm mb-1">Postal ${element.postal}</p>
                    <p class="mb-1">${routes_html}</p>
                </div>
            </a>
            `)
        });
    })
}

function loadBusTimes() {
    if (!window.location.pathname.includes('/bus/times')) return
    const bus_stop = new URLSearchParams(window.location.search).get('stop');
    $.getJSON(`/api/bus/times?bus_stop=${bus_stop}`, function(data) {
        $('#name').text(data.info.name)
        $('#postal').text(`Postal: ${data.info.postal}`)
        $('#busTimes').html('')
        data.times.forEach(element => {
            $('#busTimes').append(`
            <a class="border p-2 flex flex-wrap rounded shadow hover:bg-neutral-900 transition-all" href="/bus/routes">
                <div class="flex items-center justify-center flex-grow-0 p-2">
                    <span class="bg-green-600 text-white px-4 py-1 mr-1 rounded shadow text-2xl font-semibold">${element.route}</span>
                </div>
                <div class="flex flex-grow ml-2 items-center justify-left">
                    <div>
                        <p class="text-xl font-semibold">To ${element.destination}</p>
                        <p class="italic text-sm mb-1">Departs in: ${element.departs_in} minutes</p>
                    </div>
                </div>
            </a>
            `)
        });
    })
}

function loadBusRoutes() {
    $.getJSON(`/api/bus/routes`, function(data) {
        data.forEach(element => {
            route_html = ""
            element.route_info.forEach(element => {
                route_stops = ""
                element.stops.forEach(element => {
                    route_stops = route_stops + `${element}<br />`
                })
                route_html = route_html + `<div>${route_stops}</div>`
            })
            $('#busRoutes').append(`
            <div class="group">
                <div class="border p-2 flex flex-wrap rounded shadow group-hover:bg-neutral-900 transition-all">
                    <div class="flex items-center justify-center flex-grow-0 p-2">
                        <span class="bg-green-600 text-white px-4 py-1 mr-1 rounded shadow text-2xl font-semibold">${element.route}</span>
                    </div>
                    <div class="flex flex-grow ml-2 items-center justify-left">
                        <div>
                            <p class="text-xl font-semibold">${element.description}</p>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 max-h-0 my-2 group-hover:max-h-96 overflow-hidden transition-all duration-500">
                    ${route_html}
                </div>
            </div>
            `)
        });
    })
}

setInterval(loadBusTimes, 10000)