def add_time(start, duration, day=None):
    start_time, merid = start.split(' ')
    start_hours, start_min = start_time.split(':')
    duration_hours, duration_min = duration.split(':')
    day_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday':7}
    day_list = list(day_dict.keys())
    
    end_time_min = (int(start_min) + int(duration_min)) % 60
    extra_hours=(int(start_min) + int(duration_min)) // 60
    end_time_hours = (int(start_hours) + int(duration_hours) + extra_hours) % 12
    merid_op = (int(start_hours) + int(duration_hours) + extra_hours) // 12
    extra_days = merid_op // 2

    if merid_op % 2 == 1:
        if merid == 'AM':
            merid = 'PM'
        else:
            merid = 'AM'
            extra_days = extra_days + 1
            
    if day is not None:
        day = day.title()
        day_int = day_dict.get(day) + extra_days
        if day_int > 7:
            day_int = day_int % 7
        day_week = ', ' + day_list[day_int-1]
    else:
        day_week = None
        
    if len(str(end_time_min)) < 2:
        end_time_min='0'+str(end_time_min)
    if end_time_hours == 0:
        end_time_hours = 12
    
    end_time_days = ' ('+str(extra_days)+ ' days later)'
    end_time = str(end_time_hours) + ':' + str(end_time_min) + ' ' + merid
    
    if day_week is not None:
        end_time = end_time + day_week
    
    if extra_days == 0:
        return end_time
    elif extra_days == 1:
        end_time = end_time + ' (next day)'
    else:
        end_time = end_time + end_time_days
    
    return end_time
