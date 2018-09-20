var mockData = [
    {
        lng: 104.07547,
        lat: 30.542862,
        html: "天府五街",
        pauseTime: 2
    },
    {
        lng: 104.075945,
        lat: 30.531749,
        html: "华府大道",
        pauseTime: 2
    },
    {
        lng: 104.072352,
        lat: 30.522516,
        html: "正北上街",
        pauseTime: 2
    },
    {
        lng: 104.061842,
        lat: 30.511564,
        html: "摩尔新世纪",
        pauseTime: 2
    },
    {
        lng: 104.059003,
        lat: 30.506602,
        html: "南湖梦幻岛",
        pauseTime: 2
    },
    {
        lng: 104.057494,
        lat: 30.496987,
        html: "远大中央公园",
        pauseTime: 2
    },

];
// 实例化一个驾车导航用来生成路线

var map = new BMap.Map('map_canvas');
map.enableScrollWheelZoom();
var defaultLocation = mockData[0];
var point = new BMap.Point(defaultLocation.lng, defaultLocation.lat);
map.centerAndZoom(point, 15);
// 创建地图实例  
// 创建点坐标  
var myIcon = new BMap.Icon(
  "/static/images/location.gif",
  new BMap.Size(100, 100),
  {
    // 指定定位位置。
    // 当标注显示在地图上时，其所指向的地理位置距离图标左上
    // 角各偏移10像素和25像素。您可以看到在本例中该位置即是
    // 图标中央下端的尖角位置。
    // anchor: new BMap.Size(10, 25),
    imageSize: {
        width: 50,
        height: 50
    },
    // 设置图片偏移。
    // 当您需要从一幅较大的图片中截取某部分作为标注图标时，您
    // 需要指定大图的偏移位置，此做法与css sprites技术类似。
    // imageOffset: new BMap.Size(0, 0 - index * 25)   // 设置图片偏移
  }
);     

var points = mockData.map(function(v) {
    return new BMap.Point(v.lng, v.lat); 
});
var markers = points.map(function(v) {
   return new BMap.Marker(v, {icon: myIcon}); 
});

function setMarker(marker) {
    
    if(markers.length){
        if(marker){
            map.removeOverlay(marker);
        }

        var marker = markers.shift();
        map.addOverlay(marker);
        
        setTimeout(() => {
            setMarker(marker); 
        }, 800);
    }else{
        console.log('markers', markers);
        console.log('没有坐标了');
    }
}

setMarker();


// 获取定位数据
function getLocationOfCar(car_id) {
    var params = {
        car_id: 1,
        token: 'afoejtoket'
    };

    $.ajax({
        type: "POST",
        url: "/api/get-location",
        data: params,
        success: function (msg) {
            alert("Data Saved: " + msg);
        }
    });
}

$('#run').on('click', function () {
    getLocationOfCar('1'); 
});

