# Hadoop Mini Project: Post-Sale Automobile Report

Given an automobile history dataset, our goal was to write a MapReduce program in Python to produce a report showing the total number of accidents per make and year of car.

## Overview

The automobile data is stored in a csv in the data folder with the following schema:

| Column Name   | Type                                                  |
| ------------- | ----------------------------------------------------- |
| incident_id   | INT                                                   |
| incident_type | STRING (I: initial sale, A: accident, R: repair)      |
| vin_number    | STRING                                                |
| make          | STRING (brand; only populates with incident type 'I') |
| model         | STRING (model; only populates with incident type 'I') |
| year          | STRING (year; only populates with incident type 'I')  |
| incident_date | DATE                                                  |
| description   | STRING                                                |

### MapReduce

| Script              | Description                                                  |
| :------------------ | ------------------------------------------------------------ |
| autoinc_mapper1.py  | Input: Data from stdin<br />Output: key,value pair [vin_number   (incident_type, year, make)] |
| autoinc_reducer1.py | Input: Output of autoinc_mapper1.py<br />Output: vin_number (incident_type, year, make) filtered for "A" incident types only |
| autoinc_mapper2.py  | Input: Output of autoinc_reducer1.py<br />Output: key, value pair [concatenated string of make and year, 1] |
| autoinc_reducer2.py | Input: Output of autoinc_mapper2.py<br />Output: key (make and year) and final count of records |

### Testing

The functionality of the mapper and reducer Python scripts were tested using the Bash pipeline.

```
cat data.csv | autoinc_mapper1.py | sort | autoinc_reducer1.py | sort
```

Running the above in the terminal of your choice returns the result below. Note: Windows users can achieve the same result by using `type` instead of `cat`.

```
EXOA00341AB123456       ('A', 'Mercedes', '2016')
INU45KIOOPA343980       ('A', 'Mercedes', '2015')
VOME254OOXW344325       ('A', 'Mercedes', '2015')
VXIO456XLBB630221       ('A', 'Nissan', '2003')
```

Extending the Bash pipeline to include the 2nd MapReduce job:

```
cat data.csv | autoinc_mapper1.py | sort | autoinc_reducer1.py | sort | autoinc_mapper2.py | sort | autoinc_reducer2.py
```

```
Mercedes2015    2
Mercedes2016    1
Nissan2003      1
```

The full Bash pipeline command gives us the final product which is the number of accidents per vehicle make and year.

## Setup & Running

If you do not already have Hadoop setup on your machine, you can also run and test the code on [Hortonworks Hadoop Sandbox](https://www.cloudera.com/downloads/hortonworks-sandbox.html). I also recommend their accompanying [guide](https://www.cloudera.com/tutorials/getting-started-with-hdp-sandbox.html). Prior to running the shell script autoinc_job.sh, make sure to move the data.csv file to your file structure. Run the shell command below to do so:

```
hdfs dfs -put data.csv <destination>
```

The shell script in the src folder calls the two MapReduce jobs in sequence:

```
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-files autoinc_mapper1.py, autoinc_reducer1.py \
-mapper autoinc_mapper1.py -reducer autoinc_reducer1.py \
-input input/data.csv -output output/all_accidents

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-files autoinc_mapper2.py, autoinc_reducer2.py \
-mapper autoinc_mapper2.py -reducer autoinc_reducer2.py \
-input output/all_accidents -output output/make_year_count
```

After the job is completed we can check to see if we got the correct results by running the command:

```
hdfs dfs -cat output/make_year_count/part-00000
```
![successfulhdp](https://user-images.githubusercontent.com/41641011/115142908-0b49ef80-9ff9-11eb-91f1-2c0672e0cca9.jpg)

