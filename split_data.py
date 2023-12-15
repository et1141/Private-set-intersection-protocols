import csv

def split_date(file_name,sizes,add_padding=False):
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            total_rows = sum(1 for row in reader)
            file.seek(0)  
            ind=1
            for size in sizes:
                file.seek(0)  
                subset_size = int(size * total_rows)
                output_file_path = f"{ind}_{file_name}"
                ind+=1
                with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
                    writer = csv.writer(output_file)

                    for i, row in enumerate(reader):
                        if i < subset_size:
                            writer.writerow(row)
                        else:
                            if add_padding:
                                 for k in range (subset_size):
                                    writer.writerow(['aaaff@uwr.edu.pl','2023-03-24 05:27:19','62.7187874745721','7'])
                            break

input_file_path_bought_csv = 'bought.csv'
input_file_path_clicked_csv = 'clicked.csv'
subset_sizes =[0.2,0.4,0.6,0.8,1]
subset_sizes_2 =[0.1,0.2,0.3,0.4,0.5] #bought has only 100 000 rows inset od 200 000
split_date(input_file_path_bought_csv,subset_sizes_2,True)
split_date(input_file_path_clicked_csv,subset_sizes)
