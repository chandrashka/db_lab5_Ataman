DO $$ 
DECLARE
    i INTEGER;
BEGIN
    -- Цикл для вставки тестових даних в таблицю Track
    FOR i IN 1..5 LOOP
        INSERT INTO Track (
            track_id, track_name, artist_count, artist_id, 
            released_year, released_month, released_day, bpm, 
            key, mode, danceability_percent, valence_percent, 
            energy_percent, acousticness_percent, instrumentalness_percent, 
            liveness_percent, speechiness_percent
        )
        VALUES (
            100 + i,  -- Змінено для унікальності track_id
            'Track' || i, 
            i, 
            i, 
            2023, 
            i, 
            i, 
            100 + i, 
            i, 
            i, 
            0.7 + i * 0.1, 
            0.5 + i * 0.1, 
            0.8 - i * 0.1, 
            0.1 + i * 0.1, 
            0.2 - i * 0.1, 
            0.05 + i * 0.01, 
            0.02 + i * 0.01
        );
    END LOOP;

    -- Цикл для вставки тестових даних в таблицю Artist
    FOR i IN 1..5 LOOP
        INSERT INTO Artist (artist_name) VALUES ('Artist' || i);
    END LOOP;

    -- Цикл для вставки тестових даних в таблицю Playlist
    FOR i IN 1..5 LOOP
        INSERT INTO Playlist (track_id, in_spotify_playlists, in_apple_playlists, in_deezer_playlists) 
        VALUES (i, 1000 + i, 200 + i, 300 + i);
    END LOOP;

    -- Цикл для вставки тестових даних в таблицю Charts
    FOR i IN 1..5 LOOP
        INSERT INTO Charts (track_id, in_spotify_charts, in_apple_charts, in_deezer_charts, in_shazam_charts) 
        VALUES (i, 50 + i, 500 + i, 600 + i, 70 + i);
    END LOOP;

    -- Цикл для вставки тестових даних в таблицю Streams
    FOR i IN 1..5 LOOP
        INSERT INTO Streams (track_id, streams) VALUES (i, 1000000 + i * 100000);
    END LOOP;

END $$;