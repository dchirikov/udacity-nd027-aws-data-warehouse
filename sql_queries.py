import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

LOG_DATA = config.get("S3", "LOG_DATA")
SONG_DATA = config.get("S3", "SONG_DATA")
ARN = config.get("IAM_ROLE", "ARN")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE staging_events (
        artist              character varying(200)  ,
        auth                character varying(10)   ,
        first_name          character varying(200)  ,
        gender              character varying(1)    ,
        items_in_session    integer                 NOT NULL,
        last_name           character varying(200)  ,
        length              double precision        ,
        level               character varying(10)   NOT NULL,
        location            character varying(200)  ,
        method              character varying(10)   ,
        page                character varying(20)   NOT NULL,
        registration        double precision        ,
        session_id          integer                 NOT NULL,
        song                character varying(200)  ,
        status              integer                 NOT NULL,
        ts                  timestamp               NOT NULL,
        user_agent          character varying(200)  ,
        user_id             character varying(18)
    );
""")

staging_songs_table_create = ("""
    CREATE TABLE staging_songs (
        num_songs           bigint                  NOT NULL,
        artist_id           character varying(18)   NOT NULL,
        artist_latitude     double precision        ,
        artist_longitude    double precision        ,
        artist_location     character varying(200)  NOT NULL,
        artist_name         character varying(200)  NOT NULL,
        song_id             character varying(18)   NOT NULL,
        title               character varying(200)  NOT NULL,
        duration            double precision        NOT NULL,
        year                integer                 NOT NULL
    );
""")

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id         bigint                  IDENTITY(0, 1),
        start_time          timestamp               NOT NULL,
        user_id             character varying(18)   ,
        level               character varying(10)   NOT NULL,
        song_id             character varying(18)   NOT NULL,
        artist_id           character varying(18)   NOT NULL,
        session_id          integer                 NOT NULL,
        location            character varying(200)  ,
        user_agent          character varying(200)  ,

        primary key(songplay_id)
    );
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id             character varying(18)   NOT NULL,
        first_name          character varying(200)  NOT NULL,
        last_name           character varying(200)  NOT NULL,
        gender              character varying(1)    NOT NULL,
        level               character varying(5)    NOT NULL,

        primary key(user_id)
    );
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id             character varying(18)   NOT NULL,
        title               character varying(200)  NOT NULL,
        artist_id           character varying(200)  NOT NULL,
        year                integer                 NOT NULL,
        duration            double precision        NOT NULL,

        primary key(song_id)
    );
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id           character varying(18)   NOT NULL,
        name                character varying(200)  NOT NULL,
        location            character varying(200)  ,
        latitude            double precision        ,
        longitude           double precision        ,

        primary key(artist_id)
    );
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time          timestamp               NOT NULL,
        hour                smallint                NOT NULL,
        day                 smallint                NOT NULL,
        week                smallint                NOT NULL,
        month               smallint                NOT NULL,
        year                smallint                NOT NULL,
        weekday             smallint                NOT NULL,

        primary key(start_time)
    );
""")

# STAGING TABLES

staging_events_copy = (f"""
    copy staging_events from '{LOG_DATA}'
    credentials 'aws_iam_role={ARN}'
    gzip delimiter ';' compupdate off region 'us-west-2';
""")

staging_songs_copy = (f"""
    copy staging_songs from '{SONG_DATA}'
    credentials 'aws_iam_role={ARN}'
    gzip delimiter ';' compupdate off region 'us-west-2';
""")

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create
]

drop_table_queries = [
    staging_events_table_drop,
    staging_songs_table_drop,
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop
]

copy_table_queries = [
    staging_events_copy,
    staging_songs_copy
]

insert_table_queries = [
    songplay_table_insert,
    user_table_insert,
    song_table_insert,
    artist_table_insert,
    time_table_insert
]
