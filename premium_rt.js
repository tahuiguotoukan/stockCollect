function Premium_rt(temp1, convert_value, premium_rt)
{
    let data = [];
    temp1.forEach(v => {
        let d  = v.cell;
        let c_v = parseInt(convert_value);
        if(d.convert_value >= c_v-1 && d.convert_value <= c_v+1) data.push(d);
    })
    let value = 0;
    data.forEach(v => {
        let pre = v.premium_rt.split('%')[0]*1;
        value+=pre;
    })
    let average = value/data.length;
    let diff = (premium_rt-average)/average;
    return diff;
}
function GetList(temp1)
{
    let list = [];
    let temp1_new = temp1;
    temp1_new.forEach(v => {
        let d = v.cell;
        let diff = Premium_rt(temp1_new, d.convert_value*1, d.premium_rt.split('%')[0]*1);
        list.push({
            bond_id: d.bond_id,
            bond_nm: d.bond_nm,
            full_price: d.full_price*1,
            curr_iss_amt: d.curr_iss_amt*1,
            convert_value: d.convert_value*1,
            premium_rt: d.premium_rt.split('%')[0]*1,
            diff: Math.round(diff*100)/100,
            price: d.sprice*1,
            year_left: d.year_left*1,
            stock_nm: d.stock_nm
            
        })
    })
    //溢价偏移前30再用双低排序取前五
    list = FilterTemp1(list);
    let arr = list.sort((a, b) => {return a.diff - b.diff}).slice(0, 10);
//     arr = arr.sort((a, b) => {return b.year_left - a.year_left}).slice(0, parseInt(arr.length/2));
//     arr = arr.sort((a, b) => {return a.price - b.price}).slice(0, parseInt(arr.length/2));
//     arr = arr.sort((a, b) => {return a.full_price - b.full_price}).slice(0, parseInt(arr.length/2));
//     arr = arr.sort((a, b) => {return a.premium_rt - b.premium_rt}).slice(0, parseInt(arr.length/2));
    arr = arr.sort((a, b) => {return (a.premium_rt*100+a.full_price) - (b.premium_rt*100+b.full_price)}).slice(0, 30);
    arr = arr.sort((a, b) => {return a.diff - b.diff});
    console.table(arr);
    return arr;
}
function FilterTemp1(temp1)
{
    let list = [];
    temp1.forEach(d => {
        if(d.full_price*1 <= 114 && d.curr_iss_amt*1 > 0.3 && d.price*1 < 50 && d.stock_nm.search(/[(st)(ST)]/g) < 0){
            list.push(d);  
        };
    })
    return list;
}