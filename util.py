                    try:
                        avg_pwr =  np.apply_along_axis(avg, 2, x_train**2)
                        avg_pwr = np.apply_along_axis(avg_standarize, 1, avg_pwr, mean=csp.mean_, std=csp.std_)
                        X_train[0] = np.concatenate([X_train[0], avg_pwr], axis=1)
                    except:
                        avg_pwr =  np.apply_along_axis(avg, 2, x_train**2)
                        avg_pwr = np.apply_along_axis(avg_standarize, 1, avg_pwr, mean=csp.mean_, std=csp.std_)
                        X_train.append(avg_pwr)
                    try:
                        X_train[1] = np.concatenate([X_train[1], np.apply_along_axis(autocorr, 2, x_train)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(autocorr, 2, x_train))
                    try:
                        X_train[2] = np.concatenate([X_train[2], np.apply_along_axis(temp_centroid, 2, x_train**2)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(temp_centroid, 2, x_train**2))
                    try:
                        X_train[3] = np.concatenate([X_train[3], np.apply_along_axis(mean_abs_diff, 2, x_train)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(mean_abs_diff, 2, x_train))
                    try:
                        X_train[4] = np.concatenate([X_train[4], np.apply_along_axis(median_abs_diff, 2, x_train)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(median_abs_diff, 2, x_train))
                    try:
                        X_train[5] = np.concatenate([X_train[5], np.apply_along_axis(slope, 2, x_train)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(slope, 2, x_train))
                    try:
                        X_train[6] = np.concatenate([X_train[6], np.apply_along_axis(spectral_distance, 2, x_train)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(spectral_distance, 2, x_train))
                    try:
                        X_train[7] = np.concatenate([X_train[7], np.apply_along_axis(spectral_entropy, 2, x_train)], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(spectral_entropy, 2, x_train))
                    #fft mean coefficient
                    try:
                        X_train[8] = np.concatenate([X_train[8],
                                                     np.apply_along_axis(
                                                         fft_mean_coeff, 2,
                                                         x_train,
                                                         nfreq= 2 if csp_components>7 else 4
                                                     )], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(
                            fft_mean_coeff, 2,
                            x_train,
                            nfreq= 2 if csp_components>7 else 4
                        ))
                    #mel coeficcients
                    try:
                        X_train[9] = np.concatenate([X_train[9],
                                                     np.apply_along_axis(
                                                         mfcc, 2,
                                                         x_train,
                                                         num_ceps = 2 if csp_components>7 else 4
                                                     )],
                                                    axis=1)
                    except:
                        X_train.append(np.apply_along_axis(mfcc, 2,
                                                           x_train,
                                                          num_ceps = 2 if csp_components>7 else 4
                                                          ))
                    #wavelet abs mean
                    try:
                        X_train[10] = np.concatenate([X_train[10],
                                                      np.apply_along_axis(
                                                          wavelet_abs_mean, 2,
                                                          x_train,
                                                          widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                                                      )],
                                                     axis=1)
                    except:
                        X_train.append(np.apply_along_axis(
                                wavelet_abs_mean, 2,
                                x_train,
                                widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                        ))
                    #wavelet std
                    try:
                        X_train[11] = np.concatenate([X_train[11],
                                                      np.apply_along_axis(
                                                          wavelet_std, 2,
                                                          x_train,
                                                          widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                                                      )], axis=1)
                    except:
                        X_train.append(np.apply_along_axis(
                            wavelet_std, 2,
                            x_train,
                            widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                        ))


                    try:
                        avg_pwr =  np.apply_along_axis(avg, 2, x_test**2)
                        avg_pwr = np.apply_along_axis(avg_standarize, 1, avg_pwr, mean=csp.mean_, std=csp.std_)
                        X_test[0] = np.concatenate([X_test[0], avg_pwr], axis=1)
                    except:
                        avg_pwr =  np.apply_along_axis(avg, 2, x_test**2)
                        avg_pwr = np.apply_along_axis(avg_standarize, 1, avg_pwr, mean=csp.mean_, std=csp.std_)
                        X_test.append(avg_pwr)
                    try:
                        X_test[1] = np.concatenate([X_test[1], np.apply_along_axis(autocorr, 2, x_test)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(autocorr, 2, x_test))
                    try:
                        X_test[2] = np.concatenate([X_test[2], np.apply_along_axis(temp_centroid, 2, x_test**2)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(temp_centroid, 2, x_test**2))
                    try:
                        X_test[3] = np.concatenate([X_test[3], np.apply_along_axis(mean_abs_diff, 2, x_test)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(mean_abs_diff, 2, x_test))
                    try:
                        X_test[4] = np.concatenate([X_test[4], np.apply_along_axis(median_abs_diff, 2, x_test)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(median_abs_diff, 2, x_test))
                    try:
                        X_test[5] = np.concatenate([X_test[5], np.apply_along_axis(slope, 2, x_test)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(slope, 2, x_test))
                    try:
                        X_test[6] = np.concatenate([X_test[6], np.apply_along_axis(spectral_distance, 2, x_test)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(spectral_distance, 2, x_test))
                    try:
                        X_test[7] = np.concatenate([X_test[7], np.apply_along_axis(spectral_entropy, 2, x_test)], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(spectral_entropy, 2, x_test))
                    #fft mean coefficient
                    try:
                        X_test[8] = np.concatenate([X_test[8],
                                                     np.apply_along_axis(
                                                         fft_mean_coeff, 2,
                                                         x_test,
                                                         nfreq= 2 if csp_components>7 else 4
                                                     )], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(
                            fft_mean_coeff, 2,
                            x_test,
                            nfreq= 2 if csp_components>7 else 4
                        ))
                    #mel coeficcients
                    try:
                        X_test[9] = np.concatenate([X_test[9],
                                                     np.apply_along_axis(
                                                         mfcc, 2,
                                                         x_test,
                                                         num_ceps = 2 if csp_components>7 else 4
                                                     )],
                                                    axis=1)
                    except:
                        X_test.append(np.apply_along_axis(mfcc, 2,
                                                           x_test,
                                                          num_ceps = 2 if csp_components>7 else 4
                                                          ))
                    #wavelet abs mean
                    try:
                        X_test[10] = np.concatenate([X_test[10],
                                                      np.apply_along_axis(
                                                          wavelet_abs_mean, 2,
                                                          x_test,
                                                          widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                                                      )],
                                                     axis=1)
                    except:
                        X_test.append(np.apply_along_axis(
                                wavelet_abs_mean, 2,
                                x_test,
                                widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                        ))
                    #wavelet std
                    try:
                        X_test[11] = np.concatenate([X_test[11],
                                                      np.apply_along_axis(
                                                          wavelet_std, 2,
                                                          x_test,
                                                          widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                                                      )], axis=1)
                    except:
                        X_test.append(np.apply_along_axis(
                            wavelet_std, 2,
                            x_test,
                            widths = np.arange(1,3) if csp_components>7 else np.arange(1,5)
                        ))
