from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from Planetarium.web.forms import NewRoomForm
from Planetarium.web.models import NewRoomModel, Person


def get_taken_seats(people_in_room):
    taken_seats = []

    for person in people_in_room:
        listed_seats = transform_to_list(person.seats)
        info_person = [person.name, ]
        for row in range(len(listed_seats)):
            for col in range(len(listed_seats[row])):
                seat = listed_seats[row][col]
                if seat == 1:
                    info_person.append(['заето', row + 1, col + 1])
                elif seat == 2:
                    info_person.append(['резервирано', row + 1, col + 1])
        if len(info_person) > 1:
            taken_seats.append(info_person)
    return taken_seats


def info_seats(taken_seats):
    ready_info = []
    for person_info in taken_seats:
        first_row = []
        second_row = []
        third_row = []
        forth_row = []
        fifth_row = []
        string = ''
        to_append = []
        rows = []
        for info in person_info:
            if type(info) != list:
                to_append.append(info)
                to_append.append(' е резервирал(а)/заел(а):')
            else:
                if info[1] == 1:
                    first_row.append(info[2])
                elif info[1] == 2:
                    second_row.append(info[2])
                elif info[1] == 3:
                    third_row.append(info[2])
                elif info[1] == 4:
                    forth_row.append(info[2])
                elif info[1] == 5:
                    fifth_row.append(info[2])
        if len(first_row) > 0:
            rows.append(f'Ред 1: Място {", ".join([str(x) for x in first_row])}')
        if len(second_row) > 0:
            rows.append(f'Ред 2: Място {", ".join([str(x) for x in second_row])}')
        if len(third_row) > 0:
            rows.append(f'Ред 3: Място {", ".join([str(x) for x in third_row])}')
        if len(forth_row) > 0:
            rows.append(f'Ред 4: Място {", ".join([str(x) for x in forth_row])}')
        if len(fifth_row) > 0:
            rows.append(f'Ред 5: Място {", ".join([str(x) for x in fifth_row])}')
        to_append.append(rows)
        ready_info.append(to_append)
    return ready_info


def naming_proceed(person, mark, row, col):
    listed_seats = transform_to_list(person.seats)
    if mark == 'free':
        listed_seats[row][col] = 0
    elif mark == 'book':
        listed_seats[row][col] = 1
    else:
        listed_seats[row][col] = 2
    stringed_seats = back_to_string(listed_seats)
    if '1' not in stringed_seats and '2' not in stringed_seats:
        person.delete()
    else:
        person.seats = stringed_seats
        person.save()


def filling_proceed(row, col, mark, matrix_seats, error, name):
    default_error_message = ' Моля проверете входните си данни и опитайте отново.'
    already_taken_error = 'Това място вече е заето.'
    already_reserved_error = 'Това място вече е резервирано.'
    already_free_error = 'Това място вече е свободно.'
    invalid_seat_error = 'Не съществува такова място.'
    please_free_error = 'Моля освободете мястото преди да извършите това действие.'
    give_name_error = 'Моля въведете име на човек.'

    if check_for_invalid_seats(row, col):
        error = invalid_seat_error + default_error_message
    else:
        if mark == 'free':
            if matrix_seats[row][col] == 0:
                error = already_free_error + default_error_message
            else:
                matrix_seats[row][col] = 0
        elif mark == 'book':
            if matrix_seats[row][col] == 1:
                error = already_taken_error + default_error_message
            elif matrix_seats[row][col] == 2:
                col = f'0{col + 1}' if col / 10 < 1 else col + 1
                error = please_free_error + f' [Ред {row + 1}, Място {col}]'
            else:
                if name:
                    matrix_seats[row][col] = 1
                else:
                    error = give_name_error
        # mark = 'save'
        else:
            if matrix_seats[row][col] == 2:
                error = already_reserved_error + default_error_message
            elif matrix_seats[row][col] == 1:
                col = f'0{col + 1}' if col / 10 < 1 else col + 1
                error = please_free_error + f' [Ред {row + 1}, Място {col}]'
            else:
                if name:
                    matrix_seats[row][col] = 2
                else:
                    error = give_name_error
    return [matrix_seats, error]


def check_for_invalid_seats(row, col):
    invalid = True
    if row == 0 and 0 <= col <= 8:
        invalid = False
    elif row in [1, 3] and 0 <= col <= 10:
        invalid = False
    elif row == 2 and 0 <= col <= 11:
        invalid = False
    elif row == 4 and 0 <= col <= 6:
        invalid = False
    return invalid


def back_to_string(ll):
    result = ''
    for x in ll:
        for y in x:
            result += str(y)
        result += '|'
    return result[0:-1]


def transform_to_list(string):
    result = [[]]
    for num in string:
        if num != '|':
            result[-1].append(int(num))
        else:
            result.append([])

    return result


class IndexView(views.ListView):
    model = NewRoomModel
    template_name = 'index.html'

    extra_context = {
        'title': 'Начало',
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-number')
        return queryset


class CreateRoom(views.CreateView):
    model = NewRoomModel
    form_class = NewRoomForm
    template_name = 'create_new.html'

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('info', kwargs={
            'pk': created_object.pk,
        })


def change_the_row_in_number(row):
    if row in ['a', 'A', 'А', 'а']:
        row = 1
    elif row in ['б', 'Б', 'b', 'B']:
        row = 2
    elif row in ['с', 'С', 'c', 'C', 'ц', 'Ц']:
        row = 3
    elif row in ['d', 'D']:
        row = 4
    elif row in ['e', 'E', 'е', 'Е']:
        row = 5
    return row


def room_info_view(request, pk):
    room = NewRoomModel.objects.filter(id=pk).get()

    matrix_seats = transform_to_list(room.seats)

    seats_numbers = [
        ['01', '02', '03', '04', '05', '06', '07', '08', '09'],
        ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'],
        ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'],
        ['01', '02', '03', '04', '05', '06', '07'],
    ]

    error = None

    try:
        name = request.GET.get('name', None)
        row = request.GET.get('row', None)
        col = request.GET.get('col', None)
        mark = request.GET.get('mark', None)

        row = change_the_row_in_number(row)

        if row and col and mark:
            row -= 1
            try:
                col = int(col) - 1
                matrix_seats, error = filling_proceed(row, col, mark, matrix_seats, error, name)
            except:
                col = int(col[1]) - 1
                matrix_seats, error = filling_proceed(row, col, mark, matrix_seats, error, name)

        if not error:
            if name:
                try:
                    person = Person.objects.filter(name__icontains=name, for_room=room.pk).get()
                    naming_proceed(person, mark, row, col)
                except:
                    person = Person(
                        name=name,
                        for_room=room,
                    )
                    naming_proceed(person, mark, row, col)
            elif mark == 'free':
                people = Person.objects.filter(for_room=room).all()
                for person in people:
                    person_seats = person.seats
                    person_seats = transform_to_list(person_seats)
                    if person_seats[row][col] in [1, 2]:
                        person_seats[row][col] = 0
                        person_seats = back_to_string(person_seats)
                        person.seats = person_seats
                        person.save()
                        break
    except:
        pass

    string_seats = back_to_string(matrix_seats)
    room.seats = string_seats
    room.save()

    people_in_room = Person.objects.filter(for_room=room).all()

    taken_seats = get_taken_seats(people_in_room)

    seats_info = info_seats(taken_seats)

    context = {
        "data": NewRoomModel.objects.get(id=pk),
        'hall': matrix_seats,
        'seat_nums': seats_numbers,
        'error': error,
        'info_seats': seats_info,
    }

    return render(request, "info_room.html", context)


class EditRoom(views.UpdateView):
    model = NewRoomModel
    form_class = NewRoomForm
    template_name = 'update.html'

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('info', kwargs={
            'pk': created_object.pk,
        })


class DeleteRoom(views.DeleteView):
    model = NewRoomModel
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
