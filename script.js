Process.stdin.on('data',function(data){
    data = data.toString()
    console.log(data)
})